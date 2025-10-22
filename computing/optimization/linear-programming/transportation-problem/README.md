# Transportation Problem

## Definition

> The objective of this problem is the minimization of the total transportation cost necessary to supply *n* consumer centers from *m* supplier centers.

* $a_{i}$: available quantity at supplier *i*, $i=1,...,m.$
* $b_{j}$: required quantity at consumer center *j*, $j=1,...,n$
* $X_{ij}$: quantity to be transported from supplier center *i* to consumer center *j*;
* $c_{ij}$: cost of transporting one unit of cargo from origin *i* (supplier center) to destination *j* (consumer center);


$min~Z=\sum_{i=1}^{m}\sum_{j=1}^{n}c_{ij}x_{ij}$

subject to

$\sum_{j=1}^{n}x_{ij}=a_{i}$

$\sum_{j=1}^{m}x_{ij}=b_{j}$

$x_{ij\ge0}$ $i=1,...,m$ $j=1,...,n$

## Optimal Solution  
 * Get an initial basic feasible solution: 
   * Northwest Corner Rule;
   * Least Cost.
 * Apply Simplex;
   * The negative coefficientes in the non-basic  
   variables in objective function  means the optimal is reached.


$\sum_{i=1}^{m}\sum_{i=1}^{n}x_{ij}=\sum_{i=1}^{m}a_{i}$

$\sum_{j=1}^{n}\sum_{j=1}^{m}x_{ij}=\sum_{j=1}^{n}b_{j}$


$\sum_{i=1}^{m}a_{i}=\sum_{j=1}^{n}b_{j}$

##  [Northwest Corner Rule](https://www.youtube.com/watch?v=gZ6BQHmGC2k)  
> Begins by allocating as much as possible to the top-left cell (the "northwest" corner) and then moves right or down, filling cells in order until all supply and demand are met.  

## [Least Cost](https://www.youtube.com/watch?v=RGaGsUf_KC8)  
> Scans the entire matrix, finds the cell with the absolute lowest unit shipping cost (cij​), and allocates the maximum possible amount to it first, repeating the process with the next cheapest available cell.

## Online Solvers - Northwest Corner Rule  
* https://otimizacao.js.org/transporte.html  
* https://cbom.atozmath.com/CBOM/Transportation.aspx?q=nwcm  

## Verify Solution with file [transportation_problem.py](transportation_problem.py)