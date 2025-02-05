##  Unix Tips.
> Copyright (c) 2023-2025, Augusto Damasceno.  
> All rights reserved.   
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

# Keyboard Configuration
```bash
# Set Layout
setxkbmap -layout us
# Set Variant
setxkbmap -layout us -variant intl
setxkbmap -layout us -variant abnt2
# Switching Layouts with Caps Lock
setxkbmap -layout us,br -option grp:caps_toggle
# Adding a Compose Key (Right Alt):
#   -option compose:ralt
# Enabling Key Swap (Ctrl and Caps Lock):
#   option ctrl:swapcaps
```

# Media Player

[mpv](https://mpv.io/)

# Image Processing  
## Softwares Installation  
### ImageMagick  
```bash
# Debian
apt-get update && sudo apt-get install -y imagemagick
# Fedora
sudo dnf install -y ImageMagick
# FreeBSD
pkg install -y ImageMagick
# Arch Linux
pacman -S --noconfirm imagemagick
# MacOS
brew install imagemagick
```
* Reference: https://imagemagick.org/
### GIMP
```bash
# Debian
apt-get update && sudo apt-get install -y gimp
# Fedora
dnf install -y gimp
# FreeBSD
pkg install -y gimp
# Arch Linux
pacman -S --noconfirm gimp
# MacOS
brew install gimp
```
* Reference: https://www.gimp.org/

# Append Images
```bash
convert +append <IMG-SRC-1> ... <IMG-SRC-N> <IMG-OUTPUT>
```
* Reference: https://linux.die.net/man/1/convert

# Extract PDF Pages  
```bash
convert -density 300 <SOURCE-PDF> -quality 100 <OUTPUT-FILENAME>-%d.<FILETYPE-EXTENSION>
# Example for jpeg and pdf input.pdf
convert -density 300 input.pdf -quality 100 output-%d.jpeg
``` 
* Reference: https://linux.die.net/man/1/convert