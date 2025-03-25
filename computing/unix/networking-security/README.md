## Networking and Security in Unix-like Systems by Augusto Damasceno.
> Copyright (c) 2021-2024, Augusto Damasceno.  
> All rights reserved.   
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

# Summary
  * Use sudoedit instead of sudo EDITOR  
  * UFW Firewall  
  * Kill Switch with iptables, ufw and pf 
  * Watch a port with tshark
  * Show all listening services  
  * Kill all processes associated with a user  
  * Nmap
  * Maniputation of MAC addresses: set random vendor MAC of any kind  
  * Get Public Ip  
  * Free DNS  
  * DNS Servers and Configuration
  * NTP Servers  
  * Public Servers from ntp.br  
  * Check VPN: IP, DNS and WebRTC leaks  
  * VPN Recommendations  
  * Antivirus Recommendations  

# Use sudoedit instead of sudo EDITOR
* For Vim editor.
```bash
### Run (open the file /etc/sudoers)
sudo visudo
### Write the line
Defaults editor=/usr/bin/vim,env_editor
```
> Why?  
> sudo -e or sudoedit lets you edit a file as another user while still running the text editor as your user.  
> This is especially useful for editing files as root without elevating the privilege of your text editor.  


# UFW Firewall  
## Only allow incoming for SSH on default port
```bash
ufw --force reset
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw enable
```
## Only allow a PORT for a specific IP
> For allowing specific IPs, in some cases, it is interesting to allow only for localhost 
> and forward the local port of the service through SSH, like Jupypter and VNC services.
```bash
ufw allow from <IP> to any port <PORT>
ufw deny from any to any port <PORT> proto tcp
ufw deny from any to any port <PORT> proto udp
```
## Enable unit in systemctl and start  
```bash
systemctl enable ufw
systemctl start ufw
```

# Kill Switch with ufw, iptables, and pf

## ufw
```bash
#!/bin/bash

# Define aliases
NET_IFACE="eth0"
VPN_IFACE="tun0"
VPN_SERVER_IP="YOUR_VPN_SERVER_IP"
VPN_SERVER_PORT="YOUR_VPN_SERVER_PORT"

# Reset ufw to default settings
sudo ufw reset

# Allow traffic through the VPN interface
sudo ufw allow in on $VPN_IFACE
sudo ufw allow out on $VPN_IFACE

# Allow traffic to the VPN server
sudo ufw allow out to $VPN_SERVER_IP port $VPN_SERVER_PORT proto udp
sudo ufw allow out to $VPN_SERVER_IP port $VPN_SERVER_PORT proto tcp

# Allow local traffic
sudo ufw allow in on lo
sudo ufw allow out on lo

# Deny all other traffic
sudo ufw default deny outgoing
sudo ufw default deny incoming

# Enable ufw
sudo ufw enable
```

## iptables
```bash
#!/bin/bash

# Define aliases
NET_IFACE="eth0"
VPN_IFACE="tun0"
VPN_SERVER_IP="YOUR_VPN_SERVER_IP"
VPN_SERVER_PORT="YOUR_VPN_SERVER_PORT"

# Flush existing rules
sudo iptables -F

# Allow traffic through the VPN
sudo iptables -A OUTPUT -o $VPN_IFACE -j ACCEPT
sudo iptables -A INPUT -i $VPN_IFACE -j ACCEPT

# Allow traffic to the VPN server
sudo iptables -A OUTPUT -d $VPN_SERVER_IP -p udp --dport $VPN_SERVER_PORT -j ACCEPT
sudo iptables -A OUTPUT -d $VPN_SERVER_IP -p tcp --dport $VPN_SERVER_PORT -j ACCEPT

# Allow local traffic
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT

# Drop all other traffic
sudo iptables -A OUTPUT -o $NET_IFACE -j DROP
sudo iptables -A INPUT -i $NET_IFACE -j DROP

# Save iptables rules
sudo sh -c "iptables-save > /etc/iptables/rules.v4"
```

## pf
```bash
# Define interfaces
ext_if = "em0"
vpn_if = "tun0"
vpn_server_ip = "YOUR_VPN_SERVER_IP"
vpn_server_port = "YOUR_VPN_SERVER_PORT"

# Clear all existing rules
set skip on lo0

# Block all traffic by default
block all

# Allow traffic through the VPN interface
pass out quick on $vpn_if
pass in quick on $vpn_if

# Allow traffic to the VPN server
pass out quick on $ext_if proto udp from any to $vpn_server_ip port $vpn_server_port keep state
pass out quick on $ext_if proto tcp from any to $vpn_server_ip port $vpn_server_port keep state

# Allow local traffic
pass in quick on lo0
pass out quick on lo0
```

# Cryptography  
## GnuPG Cheat Sheet  
https://gist.github.com/augustodamasceno/94a7c8d05126f39e1ba2cc70bac22508
## Encrypt and decrypt using only a password with OpenSSL   
* Encrypt
```bash
tar cf - <FILES-OR-DIRECTORY> | openssl enc -aes-256-cbc -salt -out encrypted.tar.enc -k <PASSWORD>
```
* Decrypt
```bash
openssl enc -d -aes-256-cbc -in encrypted.tar.enc -out decrypted.tar -k <PASSWORD> && tar xvf decrypted.tar
```
## Strong cryptographically random data using OpenSSL  
### Raw
```bash
openssl rand <NUMBER-BYTES>
```
### Hexadecimal
```bash
openssl rand -hex <NUMBER-BYTES>
```
### Base 64
```bash
 openssl rand -base64 <NUMBER-BYTES>
```
 

# Watch a port with tshark
```bash
tshark -i <INTERFACE> -f "<tcp/udp> port <PORT>" -V
```

# Show all listening services
```bash
# Linux and MacOS
lsof -i -n | head -n 1; lsof -i -n | grep LISTEN;
# FreeBSD
sockstat -4l -6l
```
 
# Kill all processes associated with a user   
 ```bash
sudo pkill -TERM -u <USER>
```
 
# Nmap
## Quick Scan
```bash
nmap -T4 -F <TARGET>
```

# Maniputation of MAC addresses: set random vendor MAC of any kind
```bash
macchanger -A <INTERFACE>
```

# Get Public Ip
```bash
curl http://httpbin.org/ip 
```
or
```bash
dig +short myip.opendns.com @resolver1.opendns.com
```

# Free DNS  
https://www.noip.com  

# DNS Servers and Configuration
https://gist.github.com/augustodamasceno/f01bd47c5dc63a5e1abd1195dec1e9d2

# NTP Servers
* north-america.pool.ntp.org
* pool.ntp.org
* time.cloudflare.com
* time.google.com
* time.nist.gov
* time.apple.com
* time.windows.com
* List of Top Public Time Servers by mutin-sa  
https://gist.github.com/mutin-sa/eea1c396b1e610a2da1e5550d94b0453

# Public Servers from ntp.br 
https://gist.github.com/augustodamasceno/cc998c19338c0bbec2d0aff529e0488f

# Check VPN: IP, DNS and WebRTC leaks  
https://ipleak.net/   

#  VPN Recommendations  
* ProtonVPN  
* NordVPN  
* ExpressVPN  

# Antivirus Recommendations  
* BitDefender  
* Kaspersky  
* Norton  
* Mcafee  

# References  
* https://wiki.archlinux.org/index.php/Sudo#Editing_files  
* https://man.archlinux.org/man/sudo.8#e  
* https://www.wireshark.org/docs/man-pages/tshark.html  
* https://linux.die.net/man/1/openssl  
* https://medium.com/@emilywilliams_43022/cryptography-101-symmetric-encryption-444aac6bb7a3  
* https://opensource.apple.com/source/lsof/lsof-49/lsof/lsof.man.auto.html  
* https://man.freebsd.org/cgi/man.cgi?sockstat(1)  
* Reference: https://linux.die.net/man/1/pkill  
* https://linux.die.net/man/1/nmap  
* https://man.archlinux.org/man/community/macchanger/macchanger.1.en  