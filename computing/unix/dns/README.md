## DNS Servers and Configuration in Unix-like systems. By Augusto Damasceno.

## License
This gist note is Licensed under a [ Creative Commons Attribution 4.0 International License.](https://creativecommons.org/licenses/by/4.0/) 
## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

### Cloudflare
* 1.1.1.1

### Cisco OpenDNS
* 208.67.222.222
* 208.67.220.220

### Google
* 8.8.8.8
* 8.8.4.4

### Quad9
* 9.9.9.9
* 149.112.112.112

### Prevent changes in /etc/resolv.conf in Unix-like systems
* Stop the dhcp service
```bash
systemctl stop dhcpcd
```
* Edit the file /etc/resolv.conf with the servers you chose.
```bash
nameserver 1.1.1.1
nameserver 208.67.222.222
```
* Set the file as immutable.
```bash
chattr +i /etc/resolv.conf
```
* Start the dhcp service
```bash
systemctl start dhcpcd
```

### References
[Cloudflare](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/)  
[Cisco OpenDNS](https://www.opendns.com/setupguide/)  
[Google](https://developers.google.com/speed/public-dns)  
[Quad9](https://www.quad9.net/)  