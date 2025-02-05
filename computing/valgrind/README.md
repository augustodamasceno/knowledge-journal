# Valgrind Cheat Sheet. By Augusto Damasceno.
> Copyright (c) 2023, Augusto Damasceno.  
> All rights reserved.  
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

## Check Memory Leaks  
### leak-check  
> Keeps track of all heap blocks issued in response to calls to malloc/new et al.  
> So when the program exits, it knows which blocks have not been freed.  
### track-origins  
> keeps track of the origins of all uninitialised values  
```bash
valgrind --leak-check=full --track-origins=yes <PROGRAM>
```

## High-precision tracing profiler
```bash
valgrind --tool=cachegrind <PROGRAM>
```
> Use kcachegrind to visualize the profile. 

## References  
* https://valgrind.org/docs/manual/manual.html  
* https://valgrind.org/docs/manual/mc-manual.html#mc-manual.leaks  
* https://valgrind.org/docs/manual/cg-manual.html#cg-manual.cgopts  
* https://apps.kde.org/kcachegrind/  
* https://docs.kde.org/stable5/en/kcachegrind/kcachegrind/index.html