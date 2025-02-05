## Filesystems in Unix-like Systems. By Augusto Damasceno.

> Copyright (c) 2021-2024, Augusto Damasceno.  
> All rights reserved.   
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

# Summary  
* Report file system  
* Locate/print block device attributes    
* All contents in a directory sorted by disk usage in decreasing order  
* Total size of the current directory  
* Count all files in a directory  
* Full Disks Report and Directory Report  
* Directory Tree  
* List and Process Files  
* Find and Sed  
* Copy with rsync  
* Delete large number of files  
* Shred (gshred for macOS)  
* Compare  
* Grep  
* Sanitize CSV  
* Compress/Create Archive  
* Decompress/Extract  
* Resize Partition  
* Mount img files  

# Report file system
* Block Usage
```bash
df -h
```
* Inode information
```bash
df -i
```
* All currently mounted filesystems in a tabular format  
```bash
mount | column -t
```

# Locate/print block device attributes 
```bash
blkid
```

# All contents in a directory sorted by disk usage in decreasing order
```bash
du -sh * | sort -hr
```

# All contents in a directory sorted by disk usage in increasing order
```bash
du -sh * | sort -h
```

# Smallest content in a directory
```bash
du -sh * | sort -hr | tail -n 1
# or
du -sh * | sort -h | head -n 1
```

# Biggest content in a directory
```bash
du -sh * | sort -h | tail -n 1
# or
du -sh * | sort -hr | head -n 1
```

# Total size of the current directory
```bash
du -csh ./* | tail -n 1 
```

# Count all files in a directory  
```bash
find <DIRECTORY> -type f | wc -l
```

# Full Disks Report and Directory Report
* https://github.com/augustodamasceno/gsh/blob/main/scripts/gdisk

# File or Directory Stats
## All Stats
```bash
stat <FILE_DIRECTORY>
```
## Last Modification Timestamp (POSIX)  
```bash
stat -c %Y <FILE_DIRECTORY>
```

# Directory Tree
## Directory Tree with depth
```bash
find . -maxdepth <DEPTH> | sed -e 's/[^-][^\/]*\//  |/g' -e 's/|\([^ ]\)/|-\1/'
```
## Directory Tree with depth and sorted
```bash
find . -maxdepth <DEPTH> | sort | sed -e 's/[^-][^\/]*\//  |/g' -e 's/|\([^ ]\)/|-\1/'
```  

# List and Process Files  
## Simple Search
```bash
find <DIRECTORY> -type f -exec <COMMAND> {} \;
```
## Reccursive and Filterd Search  
> Apply a command for all files recursively inside a directory using a search pattern    
* Example for the current folder and gz files:
  * \<FILTER-TO-SEARCH\> = *.gz. 
  * \<DIRECTORY\> = .  
  * \<COMPRESS/DECOMPRESS-COMMAND\> = gunzip
```bash
find <DIRECTORY> -name '<FILTER-TO-SEARCH>' -type f | while read filename; do
    <COMPRESS/DECOMPRESS-COMMAND> "$filename"
    echo "processing $filename"
done  
```

# Find and Sed 
* Multiple filters for Python and JSON files
* Replace in place all occurrences
```bash
find <DIRECTORY> -type f \( -name "*.py" -o -name "*.json" \) -exec sed -i '' 's/<STRING-OLD>/<STRING-NEW>/g' {} \;
```

# Copy with rsync
## Secure copy a local directory to remote with
* archive (It is a quick way of saying you want recursion and want to preserve almost everything)
* verbose
* compress file data during the transfer
* create the destination folder 
```bash
rsync -avz -R -e "ssh -l <USER> -p <PORT>" <LOCAL-DIRECTORY_or_SINGLE-FILE> <USER>@<IP-OR-NAME>:<REMOTE-DIRECTORY_OR_SINGLE-FILE>
```
## Same from above from remote to local
```bash
rsync -avz -R -e "ssh -l <USER> -p <PORT>"  <USER>@<IP-OR-NAME>:<REMOTE-DIRECTORY_or_SINGLE-FILE> <LOCAL-DIRECTORY_OR_SINGLE-FILE>
```
## Local rsync: remove option -e  
```bash
rsync -avz -R <LOCAL-DIRECTORY_OR_SINGLE-FILE> <USER>@<IP-OR-NAME>:<LOCAL-DIRECTORY_OR_SINGLE-FILE>
```
## Copy a list of files preserving the directories  
```bash
OUTPUT_FOLDER="YOUR-FOLDER" 
FILE_LIST="LIST OF FILES" 
mkdir -p "$OUTPUT_FOLDER"
while IFS= read -r line; do
    rsync -R "$line" "$OUTPUT_FOLDER/"
done < "$FILE_LIST"  # Read from FILE_LIST
```

# Delete a large number of files  
```bash
# Create an empty directory
mkdir /tmp/empty
# Rsync with delete
rsync -a --delete /tmp/empty/ <Directory>
```

# Shred (gshred for macOS)
> WARNING: This operation will permanently and irreversibly delete all specified files. Use with extreme caution.
## Shred a file  
* 10 times  
* final overwrite with zeros to hide shredding   
* truncate and remove file after overwriting   
* show progress   
```bash
shred -vzu -n10
```
## Comand above for all files recursively inside a directory   
```bash
find <DIRECTORY> -type f -exec shred -vzu -n10 {} \;
```
## Comand above non-recursive
```bash
find <DIRECTORY> -maxdepth 1 -type f -exec shred -vzu -n10 {} \;
```
## Filter the find results with a STRING example for png files
```bash
find <DIRECTORY> -maxdepth 1 -type f -name "*.png" -exec shred -vzu -n10 {} \;
```

# Compare
## compare files line by line  
```bash
diff <FILE1> <FILE2>
```
## Compare common and not common lines between two files   
```bash
comm <(sort <FILE1>) <(sort <FILE2>)
```
## Compare not common lines between two files   
```bash
comm -3 <(sort <FILE1>) <(sort <FILE2>)
```
# Grep: Search file(s) for specific text  
## Search text in all files in a folder recursively with color marker, line number, and case insensitive
```bash
grep -nri --color <TEXT> <FOLDER>
```
## Search text in a file with color marker, line number, and case insensitive
```bash
grep -ni --color <TEXT> <FILE>
```
## Create a new file from a file line with a string occurency to the end of the file  
```bash
sed -n '/<STRING>/,$p' <INPUT-FILE> > <OUTPUT-FILE>
```
## Sanitize CSV  
### Print line number with different number of fields  
* Example for comma-separated and 4 fields  
```bash
separator=","
numberFields=4
awk -F"$separator" -v f="$numberFields" 'NF != f { print NR }' <FILE>
```
 
# Compress/Create Archive

* .gz (if <file>.gz already exists, use -f option)
```bash
gzip <file>
```
  
* .xz
```bash
xz <file>
```

* .tar.gz
```bash
tar -czvf <filename>.tar.gz <directory>
```

* .tar.xz
```bash
tar cf - <directory> | xz -z - > <filename>.tar.xz
```

* .zip
```bash
zip <filename>.zip <file1> <file2> <file3> 
zip -r <filename>.zip <directory>
```

* .zip in several parts
```bash
zip -0 -r -s <size-of-parts> <your-zip-filename>.zip <directory-to-zip>
```

* .lzma
```bash
lzma -c --stdout <file> > <filename>.lzma
```

* .bz2
```bash
bzip2 <file>
```

# Decompress/Extract

* .gz
```bash
gzip -d <file>.gz
```

* .gz
```bash
gzip -d <file>.gz
```

* .tar.gz
```bash
tar -vzxf <filename>.tar.gz
```

* .tar.gz especifying the files or directories
```bash
tar -vzxf <filename>.tar.gz <file1> <file2>
tar -vzxf <filename>.tar.gz <dir1> <dir2>
```

* .tar.gz to a directory
```bash
tar -vzxf <filename>.tar.gz -C <directory>
```

* .xz
```bash
xz -d <file>.xz
```

* .tar.xz
```bash
tar -xf <filename>.tar.xz
```

* zip splited in several files
```bash
7z x <first-part-filename>.z01 -o<directory>
```

* .lzma
```bash
lzma -d --stdout <file>.lzma > <filename>
```

* .bz2
```bash
bzip2 -d <file>.bz2
```

## Resize Partition

```bash
fdisk -u /dev/<device-name, like /dev/sdb>
### Copy the start-sector
d
<partition-number>
n
p
<partition-number>
### Paste the start-sector
<start-sector>
<end-sector>
w
e2fsck -f /dev/<device-and-partition, like /dev/sdb2>
resize2fs /dev/<device-and-partition, like /dev/sdb2>
```

# Mount img files

## Linux
* Get the list of partitions and offsets
```bash
fdisk -lu <img-file>
```
* Mount passing the offset (start-block times block-size)
```bash
mount -o loop,offset=<OFFSET> <img-file> <mount-point>
```
* Example: Raspberry Pi OS partition / (from https://www.raspberrypi.org) 
  * img file = 2021-03-04-raspios-buster-armhf-full.img 
  ```bash
  fdisk -lu 2021-03-04-raspios-buster-armhf-full.img                                                                                1 
  Disk 2021-03-04-raspios-buster-armhf-full.img: 8.02 GiB, 8610906112 bytes, 16818176 sectors
  Units: sectors of 1 * 512 = 512 bytes
  Sector size (logical/physical): 512 bytes / 512 bytes
  I/O size (minimum/optimal): 512 bytes / 512 bytes
  Disklabel type: dos
  Disk identifier: 0x257398ef

  Device                                    Boot  Start      End  Sectors  Size Id Type
  2021-03-04-raspios-buster-armhf-full.img1        8192   532479   524288  256M  c W95 FAT32 (LBA)
  2021-03-04-raspios-buster-armhf-full.img2      532480 16818175 16285696  7.8G 83 Linux
  ```
  * block-size = 512
  * start-block = 532480
  * mount point = /mnt
  ```bash
  sudo mount -o loop,offset=$((512*532480)) 2021-03-04-raspios-buster-armhf-full.img /mnt
  ```

## FreeBSD
* Get the list of partitions
```bash
gpart list md0
```
* Mount the partition (yeah, that easy)
```bash
file -s /dev/md0s2
```

## References:  
* https://linux.die.net/man/1/sort
* https://linux.die.net/man/1/rsync
* https://linux.die.net/man/1/grep
* https://linux.die.net/man/1/comm  
* https://linux.die.net/man/1/diff  
* https://linux.die.net/man/1/df  
* https://linux.die.net/man/1/du  
* https://linux.die.net/man/1/stat  
 
 