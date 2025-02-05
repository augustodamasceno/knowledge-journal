## How to Debug Python Code in Terminal by jdhao  
```bash
python -m pdb your_script.py
```
>    n: execute the next line  
>    p: print the value of an object  
>    s: step into a function  
>    r: return from a function  
>    b [num]: set a breakpoint at line [NUM]  
>    c: continue to run the code until a break point is met  
>    unt [NUM]: run the code until line [NUM]  
>    whatis: print the type of object (similar to p type(some_object))  
>    l: list the context of current line (default 11 lines)  
>    h: show help message  
>    q: quit the debugger  
* Reference: https://jdhao.github.io/2019/01/16/debug_python_in_terminal/  
