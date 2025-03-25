## Cryptography by Augusto Damasceno.
> Copyright (c) 2021-2025, Augusto Damasceno.  
> All rights reserved.   
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

## [GnuPG Cheat Sheet](https://github.com/augustodamasceno/knowledge-journal/blob/main/computing/gnupg/README.md)  

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
 
## Encrypt Partition with dm-crypt and LUKS (Linux Unified Key Setup)
* List the Devices
```bash
fdisk -l
```
* To delete everything and create a new partition. Example for GPT (GUID Partition Table).
```bash
echo -e "g\nn\n\n\n\nw" | sudo fdisk /dev/<DEVICE>
```
* Encrypt
```bash
 cryptsetup luksFormat /dev/<device>
 # Confirm with YES
 # Enter the passphrase
```
* Open
```bash
cryptsetup open /dev/<DEVICE> <NAME>
```
* Create a filesystem. EXT4 Example
```bash
mkfs.ext4 /dev/mapper/<NAME>
```
* Mount
```bash
mount /dev/mapper/<NAME> <DIRECTORY>
```

# References   
* https://linux.die.net/man/1/openssl  
* https://medium.com/@emilywilliams_43022/cryptography-101-symmetric-encryption-444aac6bb7a3  
* https://wiki.archlinux.org/title/Dm-crypt/Encrypting_an_entire_system  
