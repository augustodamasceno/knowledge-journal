## GnuPG Cheat Sheet. By Augusto Damasceno.

## License
This gist note is Licensed under a [ Creative Commons Attribution 4.0 International License.](https://creativecommons.org/licenses/by/4.0/) 
## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

### Generate keys
```bash
gpg --full-generate-key --expert
```

### Export Public key
```bash
gpg --output <output-filename>.pgp --armor --export <KEYID>
```

### Sent to a Keyserver
```bash  
# Command
gpg --keyserver <keyserver> --send-key <KEYID>  
# Example with MIT PGP Public Key Server
gpg --keyserver pgp.mit.edu --send-key <KEYID>  
```  

### Import with Web Key Directory (WKD)
```bash
gpg --auto-key-locate clear,wkd -v --locate-external-key user@domain
```

### Export PRIVATE key
> :warning: **Do not share or upload to the cloud!**: Use only for backup purposes.
```bash
gpg --output <output-filename>.pgp --armor --export-secret-key <KEYID>
```

### Encrypt
```bash
gpg --recipient <KEYID> --output <output-filename> --encrypt <file-to-encrypt>
```

### Sign
```bash
gpg --default-key <KEYID> --output <output-filename>.sig --sign <file-to-sign>
```

### Encrypt and sign
```bash
gpg --sign --recipient <KEYID> --output <output-filename> --encrypt <file-to-encrypt>
```

### Verify signature
```bash
gpg --verify <signature-filename>.sig <file-to-verify>
```

### Decrypt
```bash
gpg --recipient <KEYID> --output <output-filename> --decrypt <encrypted-file>
```

### Signing commits
* Configure the key
```bash
git config --global user.signingkey <KEYID>
```
* Commit
```bash
git commit -S -m your commit message
```