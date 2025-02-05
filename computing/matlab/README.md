##  Matlab Cheat Sheet. By Augusto Damasceno.  
> Copyright (c) 2021-2023, Augusto Damasceno.  
> All rights reserved.   
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

* Set breakpoint for debugging in case of error
```Matlab
dbstop if error
```

* Remove all breakpoints
```Matlab
dbclear all
```

* Save variable to the base workspace
```Matlab
assignin('base', 'var', value)
```

* Load variable from the base workspace
```Matlab
v = evalin('base', 'var')
```

* Load excel
```Matlab
myData = readtable(<excel-filename>);
```

* Load excel one time (do not load if the variable exists)
```Matlab
if exist('myData','var') == 0
    myData = readtable(<excel-filename>);
end
```

* Save all figures in png format
```Matlab
FigList = findobj(allchild(0), 'flat', 'Type', 'figure');
filename="";
for iFig = 1:length(FigList)
  FigHandle = FigList(iFig);
  set(0, 'CurrentFigure', FigHandle);
  filename = sprintf('saveFigures-%d%s', iFig, '.png');
  saveas(FigHandle, filename);
end
```

* Drop all numbers after n decimal places
```Matlab
% x is any double
x = pi; 
% n is the number of decimal places
n = 4;
% x2 is x with all decimal places from n+1 droped
x2 = fix(x * 10^n) / 10^n;
```

* Simple Graph 
```Matlab
x = 1:100;
y = sin(x);
figure(1)
plot(x, y,'linewidth',2);
title('TITLE','fontsize', 14)
xlabel('XAXIS','fontsize', 12)
ylabel('YAXIS','fontsize', 12) 
figure(1)
saveas(gcf, 'TITLE.fig')
```

* Try Catch  
> https://www.mathworks.com/help/matlab/ref/try.html?s_tid=doc_ta   

```Matlab
try
    a = notaFunction(5,6);
catch ME
    switch ME.identifier
        case 'MATLAB:UndefinedFunction'
            warning('Function is undefined.  Assigning a value of NaN.');
            a = NaN;
        case 'MATLAB:scriptNotAFunction'
            warning(['Attempting to execute script as function. '...
                'Running script and assigning output a value of 0.']);
            notaFunction;
            a = 0;
        otherwise
            rethrow(ME)
    end
end
```