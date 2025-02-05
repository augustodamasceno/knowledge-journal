# SSH
## Generate EdDSA (Twisted Edwards curve) keys
```bash
ssk-keygen -t ed25519 -C "user@email"
```
## Identify port and key
```bash
ssh <USER>@<IP-or-NAME> -p <PORT> -i <PRIVATE-KEY> 
```
## Configure port and keys for hosts
> Edit file .ssh/config. Example
```
Host github.com
    User git
    Hostname github.com
    Port 22
    IdentityFile ~/.ssh/id_ed25519
```
## Local port forwarding
```bash
ssh -L  <LOCAL-PORT>:localhost:<REMOTE-PORT> <USER>@<IP> -p <PORT> -i <PRIVATE-KEY> 
```
## SOCKS proxy
```bash
ssh -D  <SOCKS-PORT> <USER>@<IP> -p <PORT> -i <PRIVATE-KEY> 
```
