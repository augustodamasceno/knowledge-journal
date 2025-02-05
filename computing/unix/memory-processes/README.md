## Memory and Processes in Unix-like Systems by Augusto Damasceno.
> Copyright (c) 2021-2024, Augusto Damasceno.  
> All rights reserved.   
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

## Memory
## Display amount of free and used memory in the system
```bash
free -h
```

## System memory info: file /proc/meminfo

## htop - interactive process viewer  

## TOP 3 MEMORY USE (for more change the head -<N>)
```bash
ps aux | head -1
ps aux | sort -rn -k 4,6 | head -3
```

## The sum of all RSS (Resident Set Size) of the processes' memory with a string in the command name
```bash
ps -e -o rss,comm | grep <STRING> | awk '{print $1}' | paste -sd+ - | bc | awk '{ printf "%.2fMB\n", $1/1024 }'
```

# CPU

## TOP 3 CPU USE (for more change the head -\<N\>)
```bash
ps aux | head -1
ps aux | sort -rn -k 3,6 | head -3
```

# Processes
## Get a process PID by name
```bash
ps aux | grep <NAME>
# or
pgrep <NAME>
```
  
## Process Threads
```bash
ps -T -p PID
```
  
## Force a process to terminate by pid
```bash
kill -9 PID
```

## Process terminate by name
```bash
pkill <NAME>
```

## Interative process kill.  
https://github.com/augustodamasceno/gsh/blob/main/scripts/ikill

## Change process priority (nice value range: [-20, 19]), -20 is the highest
```bash
renice -n <NICE_VALUE> -p $pid
```
  
##  Performance analysis tools for Linux  
> Read Perf events and tool security in reference 6.  

* Record a program  
```bash
perf record ./<PROGRAM>
```  

* Report from a perf data  
>  perf record creates perf.data and backup the old one  
```bash
perf report -i <PERF-DATA>
```

* Report graph in a hierarchical/tree-like format
```bash
perf report -i <PERF-DATA> --stdio --hierarchy
```

### References: 
* 1. https://linux.die.net/man/1/ps
* 2. https://linux.die.net/man/1/pkill
* 3. https://linux.die.net/man/1/kill
* 4. https://man7.org/linux/man-pages/man2/nice.2.html
* 5. https://linux.die.net/man/1/htop  
* 6. https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html   
* 7. https://man7.org/linux/man-pages/man1/perf.1.html   