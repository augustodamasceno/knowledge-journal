// Linear Programming Graphical Solution
// This file is part of the Knowledge Journal 
// See https://github.com/augustodamasceno/knowledge-journal/
// Copyright (c) 2025, Augusto Damasceno.
// All rights reserved.
// SPDX-License-Identifier: BSD-2-Clause
//------------------------------------------------------------

// Definition
// Maximize: z = 12*x1 + 15*x2
// Constrains:
// c1: x1 + 3*x2 <= 13
// c2: x1 + x2   <= 6
// c3: x1        <= 3
// c4: x1        >= 0
// c5: x2        <= 4
// c6: x2        >= 0

clc;
close

title("Linear Programming Graphical Solution");
xlabel("x1");
ylabel("x2");
xgrid();

N = 2;
x1 = linspace(0, 3, N);
x2 = linspace(0, 4, N);
x2_c1 = (13 - x1) / 3;
x2_c2 = 6 - x1;
x1_c3 = 3*ones(N, 1);
x1_c4 = zeros(N, 1);
x2_c5 = 4*ones(N, 1);
x2_c6 = zeros(N, 1);

// Constrain 1:  x1 + 3*x2 <= 13
plot(x1, x2_c1, 'b-', "thickness", 2);
// Constrain 2: x1 + x2   <= 6
plot(x1, x2_c2, 'b--', "thickness", 2);
// Constrain 3:  x1        <= 3
plot(x1_c3, x2, 'm', "thickness", 2);
// Constrain 4:  x1        >= 0
plot(x1_c4, x2, 'm', "thickness", 2);
// Constrain 5: x2        <= 4
plot(x1, x2_c5, 'm', "thickness", 2);
// Constrain 6: x2        >= 0
plot(x1, x2_c6, 'm', "thickness", 2);

// Vertice O
xstring(0.01, 0.01, 'O');
plot(0, 0, 'ko')
// Vertice A
xstring(0.01, 4.01, 'A');
plot(0, 4, 'ko')
// Vertice B
xstring(1.01, 4.01, 'B');
plot(1, 4, 'ko')
// Vertice C
xstring(2.51, 3.51, 'C');
plot(2.5, 3.5, 'ko')
// Vertice D
xstring(3.01, 3.01, 'D');
plot(3, 3, 'ko')
// Vertice E
xstring(3.01, 0.01, 'E');
plot(3, 0, 'ko')

// Best Vertice
z_max = 82.5
x2_zmax = -(4/5)*x1 + z_max/15;
plot(x1, x2_zmax, 'r-.', "thickness", 2);

set(gca(),'data_bounds',[min(x1),min(x2); max(x1)+1,max(x2)+1])
legend(['x1 + 3*x2 <= 13', ...
        'x1 + x2   <= 6', ...
        'x1 <= 3', ...
        'x1 >= 0', ...
        'x2 <= 4' ...
        'x2 >= 0' ...
        'O' ...
        'A' ...
        'B' ...
        'C' ...
        'D' ...
        'E' ...
        'Z Max Value = 82.5']);
