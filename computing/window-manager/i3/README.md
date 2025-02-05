# i3

## Proposal of an i3status configuration file.  
> File: i3status.conf  


![Screenshot](screenshot.png)  


## i3 Window Manager Cheat Sheet by @JeffPaine
> Link: https://gist.github.com/JeffPaine/cbdf57c3721546b14113  
> File [i3-cheat-sheet.md](i3-cheat-sheet.md)  

### Print Screen
* Install scrot
* Put in the file ~/.config/i3/config:
```bash
bindsym Print exec scrot $HOME/printscreen`date +%d-%m-%Y_%H-%M-%S`.png
```
* The png image will be placed in the home folder with the name  
printscreen with the date, like "printscreen22-07-2021_15-56-35.png"