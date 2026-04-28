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
## Custom names (SSH aliases)
> Use custom names in ~/.ssh/config to simplify SSH connections

### Example: Create an alias
```
Host myserver
    HostName 192.168.1.100
    User myuser
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
```

### Usage
```bash
# Instead of: ssh myuser@192.168.1.100 -p 2222 -i ~/.ssh/id_ed25519
ssh myserver
```

### Multiple aliases
```
Host dev
    HostName dev.example.com
    User developer
    IdentityFile ~/.ssh/dev_key

Host prod
    HostName prod.example.com
    User produser
    IdentityFile ~/.ssh/prod_key

Host testing
    HostName testing.internal
    User testuser
    Port 2222
```

### Connect using alias
```bash
ssh dev
ssh prod
ssh testing
```

## Local port forwarding
```bash
ssh -L  <LOCAL-PORT>:localhost:<REMOTE-PORT> <USER>@<IP> -p <PORT> -i <PRIVATE-KEY> 
```
## SOCKS proxy
```bash
ssh -D  <SOCKS-PORT> <USER>@<IP> -p <PORT> -i <PRIVATE-KEY> 
```
