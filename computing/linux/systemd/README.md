# systemd  
## Example of service calling the binary /usr/bin/mybin at system start
* Create the file /etc/systemd/system/myservice.service
```bash
[Unit]
Description=The description of the service

[Service]
Type=simple
User=root
ExecStart=/usr/bin/mybin
Restart=always

[Install]
WantedBy=multi-user.target
```
* Set permissions  
```bash
chmod 0644 /etc/systemd/system/myservice.service
```
* Enable, start, and see the status of the service
```bash
sudo systemctl enable myservice.service  
sudo systemctl start myservice.service  
sudo systemctl status myservice.service
```
# References
* https://man.archlinux.org/man/systemd.1.en