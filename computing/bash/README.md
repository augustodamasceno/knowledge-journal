## Notes - Bash. By Augusto Damasceno.
> Copyright (c) 2023, 2024, Augusto Damasceno.  
> All rights reserved.  
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

## Gin Shell or GSH - My collection of bash scripts.
> When creating bash scripts or aliases, avoid doing simple tasks and use the program args to keep reminding of them.  
* https://github.com/augustodamasceno/gsh

## ShellCheck, a static analysis tool for shell scripts 
* https://github.com/koalaman/shellcheck

## Gin Shell or GSH - My collection of bash scripts.
* https://github.com/augustodamasceno/gsh

## Status
* Exit status of the most recently executed foreground pipeline.
```bash
echo $? 
```

## Files
### Empty out a file
```bash
truncate -s 0 <FILE>
```
### Set a file as immutable.
```bash
chattr +i <FILE>
```
### Test if a directory exists
```bash
[ -d <DIRECTORY> ]
```
### Test if a file exists
```bash
test -f <FILE>
```

## Command output to the clipboard using X  
* Needs xsel
```bash
echo "OUTPUT" | xsel --clipboard --input
```

## Commands to extract a text file portion between the first and before last appearances of two specific strings.
> Good for files with timestamps.   
> Note this command does not work if one of the strings does not exist 
> in the file or the first occurrence of the second string happens before the first one.
* First line occurrence  
```bash
grep -n -m 1 "$STRING_START" $FILE | awk -F':' '{print $1}'
```
* Last line occurrence  
```bash
grep -n -m 1 "$STRING_END" $FILE | awk -F':' '{print $1}'
```
* Extract the lines [START, END[  
```bash
awk 'NR>=FISRT && NR<LAST' <FILE> > <OUTPUT>
```
* GSH Script with this logic: https://github.com/augustodamasceno/gsh/blob/main/scripts/gtxt-selection  

## References: 
* https://linux.die.net/man/1/bash  
* https://github.com/koalaman/shellcheck  
* https://github.com/augustodamasceno/gsh