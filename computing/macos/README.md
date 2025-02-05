## Notes about macOS. By Augusto Damasceno.
> Copyright (c) 2023, 2024, Augusto Damasceno.  
> All rights reserved.  
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

## Create installation media from Terminal  
> Example for Sonoma 14  
* Download the macOS from App Store  
macappstores://apps.apple.com/app/macos-sonoma/id6450717509?mt=12
Run
```bash
sudo /Applications/Install\ macOS\ Sonoma.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume
```
* Older versions and links  
> https://support.apple.com/en-us/HT211683

## At install use full disk encryption

* Encrypt Devices  
> https://support.apple.com/guide/disk-utility/encrypt-protect-a-storage-device-password-dskutl35612/mac

## keyboards Shortcuts  
* https://support.apple.com/en-us/HT201236

## Firewall  
* https://objective-see.org/products/lulu.html

## Screenshots with annotations  
* https://getgreenshot.org/

## Image Editor    
* https://www.gimp.org/

## Media Player  
* https://www.videolan.org/

## Torrent  
* https://transmissionbt.com/

## Disk Usage 
* https://grandperspectiv.sourceforge.net/
* https://apps.apple.com/br/app/grandperspective/id1111570163?l=en&mt=12

## Homebrew - The Missing Package Manager for macOS  
* https://brew.sh/
* https://github.com/Homebrew/brew/

## Generating thumbnails by reseting the Quick Look server  
```bash
qlmanage -r
```

## Raw image processing application that supports a wide range of raw formats  
> https://www.rawtherapee.com/

## Functionalities to read, manipulate, and render PDF files
> poppler

## macFUSE - Allows you to extend macOS's native file handling capabilities via third-party file systems.   
* https://osxfuse.github.io/
* https://github.com/osxfuse/osxfuse

## Android File Transfer for macOS  
* https://github.com/ganeshrvel/openmtp

## sshfs
* https://github.com/osxfuse/sshfs/releases
* https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh

## LLVM Brew
```bash
echo 'export PATH="/usr/local/opt/llvm/bin:$PATH"' >> ~/.zshrc
export LDFLAGS="-L/usr/local/opt/llvm/lib"
export CPPFLAGS="-I/usr/local/opt/llvm/include"
```

## GDB
* https://gist.github.com/mike-myers-tob/9a6013124bad7ff074d3297db2c98247
+
* Add Your User to the _developer Group:
```bash
sudo dscl . append /Groups/_developer GroupMembership $(whoami)
```

## Apache HTTP Server (Built-in)  
* Start
```bash
sudo apachectl start
```

* Stop
```bash
sudo apachectl stop
```

* Apache serves files from 
> /Library/WebServer/Documents

* Apache configuration file
/etc/apache2/httpd.conf