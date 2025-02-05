# LaTeX Cheat Sheet  
> Copyright (c) 2023, Augusto Damasceno.  
> All rights reserved.  
> SPDX-License-Identifier: CC-BY-4.0  

## All LaTeX (1) commands works well in Overleaf (2).

## PDF Metadata
* Preamble
```latex
\usepackage[ pdftitle={TITLE},
pdfsubject={SUBJECT},
pdfkeywords={KEYWORDS},
pdfauthor={AUTHOR},
hidelinks]{hyperref}
``` 


## Equations
* Packages
```latex
\usepackage{amsmath}
\usepackage{amsfonts}
```
* Example
```latex
\eqref{eq:equation-label}

\begin{equation}\label{eq:equation-label}
  y = x
\end{equation}
```
* Example with Conditions
```latex
\eqref{eq:fibonacci}

\begin{equation}\label{eq:fibonacci}
\begin{array}{ c l }
F(n) = F(n-1) + F(n-2) & F(0) = 0 \\
                 & F(1) = 1 \\
\end{array}
\end{equation}
```
* Example with Cases
```latex
\[
f(x) =
\begin{cases}
    0 & \text{if $x=0$,}\\
    1 & \text{otherwise.}
\end{cases}
\]
```

## Matrix
* Packages
```latex
\usepackage{amsmath}
\usepackage{amsfonts}
```
* Example
```latex
\begin{pmatrix}
a11 & a12 & a13 \\
a21 & a22 & a23 \\
a31 & a32 & a33
\end{pmatrix}
```

## Pseudocode
* Package
```latex
\usepackage{algpseudocode}
```
* Example
```latex
\begin{algorithmic}[1]
\State $i \gets 10$
\If{$i\geq 5$} 
    \State $i \gets i-1$
\Else
    \If{$i\leq 3$}
        \State $i \gets i+2$
    \EndIf
\EndIf 
\end{algorithmic}
```

## Code
* Package
```latex
\usepackage{listings}
```
* Options
> \lstset{hkey=value listi}
* Options Example (4)
```latex
\lstset{
  language=C,                % choose the language of the code
  numbers=left,                   % where to put the line-numbers
  stepnumber=1,                   % the step between two line-numbers.        
  numbersep=5pt,                  % how far the line-numbers are from the code
  backgroundcolor=\color{white},  % choose the background color. You must add \usepackage{color}
  showspaces=false,               % show spaces adding particular underscores
  showstringspaces=false,         % underline spaces within strings
  showtabs=false,                 % show tabs within strings adding particular underscores
  tabsize=2,                      % sets default tabsize to 2 spaces
  captionpos=b,                   % sets the caption-position to bottom
  breaklines=true,                % sets automatic line breaking
  breakatwhitespace=true,         % sets if automatic breaks should only happen at whitespace
  title=\lstname,                 % show the filename of files included with \lstinputlisting;
}
```
* Example with C Code
```latex
\begin{lstlisting}[language={[ansi]C}]
#include <stdio.h>

int main() {
   printf("Hello, World!");
   return 0;
}
\end{lstlisting}
```
* Example with C Code from File
```latex
\lstinputlisting{file-with-code.c}
```

## Language
* Command
```latex
\usepackage[IDIOM]{babel}
```
* Brazilian Portuguese Example
```latex
\usepackage[brazil]{babel}
```
* Multilingual Example
```latex
\usepackage[english,french]{babel}
``` 

## Bibliography Management
* Packages
```latex
\usepackage{biblatex}
\usepackage{csquotes}
``` 
* Preamble
```latex
\bibliography{THE-BIBLIOGRAPHY-FILE-WITHOUT-FILE-FORMAT}
``` 
* Preamble Example for the Bibliography File *myrefs.bib*
```latex
\bibliography{myrefs}
```
* Print the Bibliography
```latex
\printbibliography
``` 
* Bibliography File Example (6)
```latex
@article{einstein,
    author = "Albert Einstein",
    title = "{Zur Elektrodynamik bewegter K{\"o}rper}. ({German})
    [{On} the electrodynamics of moving bodies]",
    journal = "Annalen der Physik",
    volume = "322",
    number = "10",
    pages = "891--921",
    year = "1905",
    DOI = "http://dx.doi.org/10.1002/andp.19053221004",
    keywords = "physics"
}

@book{dirac,
    title = {The Principles of Quantum Mechanics},
    author = {Paul Adrien Maurice Dirac},
    isbn = {9780198520115},
    series = {International series of monographs on physics},
    year = {1981},
    publisher = {Clarendon Press},
    keywords = {physics}
}

@online{knuthwebsite,
    author = "Donald Knuth",
    title = "Knuth: Computers and Typesetting",
    url  = "http://www-cs-faculty.stanford.edu/~uno/abcde.html",
    addendum = "(accessed: 01.09.2016)",
    keywords = "latex,knuth"
}

@inbook{knuth-fa,
    author = "Donald E. Knuth",
    title = "Fundamental Algorithms",
    publisher = "Addison-Wesley",
    year = "1973",
    chapter = "1.2",
    keywords  = "knuth,programming"
}
```

## Enumerate with Letters or Only Numbers
* Package
```latex
\usepackage{enumitem}
```
* Example with Lowercase
```latex
\begin{enumerate}[label=\alph*]
    \item First
    \item Second
\end{enumerate}
```
* Example with Uppercase
```latex
\begin{enumerate}[label=\Alph*]
    \item First
    \item Second
\end{enumerate}
```
* Example Forcing Numbers
```latex
\begin{enumerate}[label*=\arabic*.]
    \item First
    \item Second
\end{enumerate}
```

## One sided (For Prints in One Side) and Two Sided (Chapters in Odd Pages and a Blank Page After) Document.
* One Sided Example (Preamble Command) for Article Document.
```latex
\documentclass[oneside]{article}
```
* Two Sided Example (Preamble Command) for Article Document.
```latex
\documentclass[twoside]{article}
```

## References
1.https://www.latex-project.org  
2.https://www.overleaf.com  
3.https://ctan.org/pkg/listings?lang=en  
4.https://stackoverflow.com/questions/4439605/c-source-code-in-latex-document  
5.https://ctan.org/pkg/babel?lang=en  
6.https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX  
7.https://ctan.org/pkg/enumitem?lang=en  
8.https://www.overleaf.com/learn/latex/Single_sided_and_double_sided_documents  