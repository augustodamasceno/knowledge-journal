# Arch Linux

## Install AUR Packages. By Augusto Damasceno.

> Licensed under a [ Creative Commons Attribution 4.0 International License.](https://creativecommons.org/licenses/by/4.0/) 

### Install base-devel package group
pacman -S --needed base-devel

### Download the package the build files
makepkg -si

### Example - Installing Snap
*  Download Snapshot  
    [https://aur.archlinux.org/packages/snapd/](https://aur.archlinux.org/packages/snapd/)   
* Go to the download folder and run:
    ```bash
    tar vzxf snapd.tar.gz
    cd snapd
    makepkg -si
    ```

```
Warning
AUR packages are user produced content. 
These PKGBUILDs are completely unofficial and have not been thoroughly vetted. 
Any use of the provided files is at your own risk.
```

## Thumbnails for Arch with Linux Hardened
```bash
pacman -S bubblewrap-suid 
pacman -S ffmpegthumbnailer gst-libav gst-plugins-ugly
rm -rf  ~/.cache/thumbnails/fail/
```


## References:

1. https://wiki.archlinux.org/index.php/Arch_User_Repository
2. https://archlinux.org/groups/x86_64/base-devel/
3. https://wiki.archlinux.org/index.php/Snap
4. https://wiki.archlinux.org/title/GNOME/Files#Thumbnails