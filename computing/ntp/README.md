## Public Server from ntp.br. By Augusto Damasceno.

## License
This gist note is Licensed under a [ Creative Commons Attribution 4.0 International License.](https://creativecommons.org/licenses/by/4.0/) 
## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

### Add to /etc/ntp.conf
```bash
server a.st1.ntp.br iburst
server b.st1.ntp.br iburst
server c.st1.ntp.br iburst
server d.st1.ntp.br iburst
server gps.ntp.br iburst
server a.ntp.br iburst
server b.ntp.br iburst
server c.ntp.br iburst
```

### Sync
ntpdate -u a.st1.ntp.br

### References

* [https://ntp.br/guia-linux-avancado.php](https://ntp.br/guia-linux-avancado.php)