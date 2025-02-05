# GDB Cheat Sheet. By Augusto Damasceno.
> Copyright (c) 2023, 2024, Augusto Damasceno.  
> All rights reserved.  
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

## Compile C code with optiong "g" to produce debugging information in the operating system's native format.
```bash
gcc -o <OUTPUT> <C-SOURCE> -g 
```

## Set break point
```gdb
break <SYMBOL>
or
b <SYMBOL>
```

## Set break point for shared libraries  
```gdb
break dlopen
```


## Set break point with conditon
```gdb
b <LINE> if i == 7
```

## Show breakpoints  
```gdb
info break
```

## Run to break point
```gdb
run
# or
r
```

## Execute next line in C code
```gdb
next
```

## Execute next line in assembly code
```gdb
nexti
```

## Step in
```gdb
step
```

## Step out
```gdb
finish
```

## Jump to a reference, file:line or memory
```gdb
jump <REFERENCE_FILE:LINE_MEMORY>
```

## Print a value
```gdb
print <EXPRESSION>
# or
p <EXPRESSION>
```

## Print an array
```gdb
p *array@len
```

## Pretty print arrays
```gdb
set print array on
# disable 
set print array off
```

## Pretty print structures  
```gdb
set print pretty on
# disable
set print pretty off
```

## View code in text user interface  
```gdb
layout src 
```

## View the assembly code in text user interface   
```gdb
 layout asm
```

## Refresh the screen
```gdb
refresh
# or
ref
```

## Displays the assembly code for the current function
```gdb
disassemble
```

## Print a stack trace
```gdb
backtrace
# or
bt
# or
info stack
# or
where
```

## Memory address space ranges  
```gdb
info proc mappings
```

## Examine Memory
```gdb
x/i <ADDRESS>
```

## Show registers information
```gdb
info registers
```

## Show stack frame  
```gdb
info frame
```

## Show functions signatures  
```gdb
info functions
```

## Attach to a running process  
```gdb
gdb -p <PID>
```

## Copy from memory to file (DUMP)  
* Format  
> binary: Raw binary form.   
> ihex: Intel hex format.   
> srec: Motorola S-record format.   
> tekhex: Tektronix Hex format.   
> verilog: Verilog Hex format.  
>  If format is omitted, GDB dumps the data in raw binary form.   
```bash
dump <FORMAT> memory <FILENAME> <START_ADDRESS> <END_ADDRESS>
dump <FORMAT> value <FILENAME> <EXPRESSION>
```

## References:
* https://sourceware.org/gdb/current/onlinedocs/gdb.html/
* https://sourceware.org/gdb/current/onlinedocs/gdb.html/Arrays.html
* https://sourceware.org/gdb/current/onlinedocs/gdb.html/Process-Information.html  
* https://linux.die.net/man/1/gcc
* https://linux.die.net/man/1/gdb
* https://sourceware.org/gdb/current/onlinedocs/gdb.html/Dump_002fRestore-Files.html#Dump_002fRestore-Files
* [ GDB is REALLY easy! Find Bugs in Your Code with Only A Few Commands by LowLevelLearning Youtube Channel](https://www.youtube.com/watch?v=Dq8l1_-QgAc)  
* [Working GDB on macOS 11 by mike-myers-tob](https://gist.github.com/mike-myers-tob/9a6013124bad7ff074d3297db2c98247)