## Notes - Python Numba AOT. By Augusto Damasceno.
> Copyright (c) 2023, Augusto Damasceno.  
> All rights reserved.  
> SPDX-License-Identifier: CC-BY-4.0  

### Dependencies
* setuptools
* numpy
* llvmlite

## nopython mode
> A Numba compilation mode that generates code that does not access the Python C API. 
> This compilation mode produces the highest performance code, 
> but requires that the native types of all values in the function can be inferred. 
> Unless otherwise instructed, the @jit decorator will automatically fall back to object mode 
> if nopython mode cannot be used.

## Supported NumPy features  
* https://numba.pydata.org/numba-doc/latest/reference/numpysupported.html  

## For more optimization, change some numpy calls for simple loops.  

## [:] indicates the arg is a 1D array. Use [:, :] for 2D arrays.  

## Use Tuple(type, type, ...) to return several objects.  

## To support several types in the same implementation add more decorators with respective signatures and add a suffix to the name.  
```python
@njit()
@cc.export('maxi', 'i8(i8[:])')
@cc.export('maxf', 'f8(f8[:])')
def max(data):
    return np.nanmax(data)
```

## Example with sum of squares  
### Run to compile.  
```python
from numba import njit
from numba.pycc import CC

import numpy as np

# class numba.pycc.CC(extension_name, source_module=None)
cc = CC('my_module')

 
# @export(exported_name, sig)
@njit
@cc.export('sq_sum', 'f8(f8[:])')
def sq_sum(data):
    val = 0.0
    for item in data:
        val += item * item
    return val


if __name__ == "__main__":
  cc.compile()
```

### Usage
```python
import numpy as np
import my_module

my_module.sq_sum(np.array([1.0, 2.0, 3.0]))
```
>  Note that run "my_module.sq_sum(np.array([1, 2, 3]))" will return zero as the function signature is for float, not int.

### Execution Time Comparison  
```python
import timeit
import math

import numpy as np

import my_module


if __name__ == "__main__":
  np.random.seed(10)
  data = np.random.random(int(10**6))

  pure_python_mean_time = timeit.timeit(lambda: sum([item**2 for item in data]), number=100) 
  numpy_mean_time = timeit.timeit(lambda: np.sum(data**2.0), number=100)
  numba_aot_mean_time = timeit.timeit(lambda: my_module.sq_sum(data), number=100)

  print(f"Pure Python mean time: {pure_python_mean_time:.6f} seconds") 
  print(f"Numpy mean time: {numpy_mean_time:.6f} seconds")
  print(f"Numba AOT mean time: {numba_aot_mean_time:.6f} seconds")
```
#### Machine
> OS: Debian GNU/Linux 12 (bookworm)  
> Kernel version: 6.1.0-10-amd64  
> CPU: Intel Core Processor (Broadwell, no TSX, IBRS)  
> RAM: 451Mi  
#### Output
> Pure Python mean time: 25.355708 seconds  
> Numpy mean time: 0.140131 seconds  
> Numba AOT mean time: 0.117810 seconds  

## Important!
> When using NumPy functions like sum, it's worth noting that these functions are already highly optimized, 
> leveraging efficient C implementations internally. 
> For such well-optimized operations, additional Ahead-of-Time (AOT) compilation may not yield substantial 
> performance gains. NumPy's built-in optimizations often provide excellent performance, 
> and it's essential to consider the specific use case before exploring further optimization.

## References  
* https://numba.pydata.org/numba-doc/latest/reference/  
* https://numba.pydata.org/numba-doc/latest/user/installing.html
* https://numba.pydata.org/numba-doc/latest/reference/aot-compilation.html
* https://numba.pydata.org/numba-doc/latest/glossary.html#term-nopython-mode