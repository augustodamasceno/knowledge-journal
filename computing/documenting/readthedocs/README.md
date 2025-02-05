## Documentation with readthedocs.io by Augusto Damasceno.
> Copyright (c) 2023,2024, Augusto Damasceno.  
> All rights reserved.   
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

# Document the code with reStructuredText. Example:
```reStructuredText
    """
    The sum of integers.

    Parameters
    ----------
    - A : int
        left operator.
    - B :  int
        right operator.

    Returns
    -------
    - int
        A + B.
        
    Raises
    -------
    - TypeError
      When an operand type is unsupported.
    """
```

# Generate Documentation with Sphinx
* Setting up the documentation sources
```bash
sphinx-quickstart
```
* Add extension for autodoc. Edit extensions in the file `docs/source/conf.py`
```Python
extensions = [
    'sphinx.ext.autodoc',
]
```
* Automatic generation of Sphinx sources  
```bash
sphinx-apidoc -o <OUTPUT_PATH> <MODULE_PATH>
```
* Put the sources entries for doc in `docs/source/index.rst`
* Genarate HTML Doc Page  
```bash
cd docs && make html
```

# Create a readthedocs.io account and link with you GitHub repository  

# References  
* https://www.sphinx-doc.org
* https://readthedocs.io 