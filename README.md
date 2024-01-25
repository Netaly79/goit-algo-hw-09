# goit-algo-hw-09

Розглянемо швидкість роботи алгоритмів для 1234567

For  1234567  cents, using greedy algorithm:  {50: 24691, 10: 1, 5: 1, 2: 1}
Find Coins Greedy Time: 0.0001  seconds
For  1234567  cents, using find_min_coins algorithm:  {2: 1, 5: 1, 10: 1, 50: 24691}
Find Min Coins Time: 1.8827  seconds


Збільшемо значення у 10 разів:

For  12345670  cents, using greedy algorithm:  {50: 246913, 10: 2}
Find Coins Greedy Time: 0.0001  seconds
For  12345670  cents, using find_min_coins algorithm:  {10: 2, 50: 246913}
Find Min Coins Time: 18.5046  seconds



Теоретично, жадібний алгоритм має складність О(nlogn), а динамічний - О(n), але в даному випадку перший працює набагато скоріше, тому що не створює таблицю з великою кількістю даних.
Збільшення значення у 10 разів пропорційно збільшує час виконання динамічного алгоритма.
