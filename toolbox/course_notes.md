# Github solutions examples

https://github.com/anoubhav/Coursera-Algorithmic-Toolbox

# Course1

* O-notation 
* Greedy Algorithms
* Divide and Conquer
* Dynamic Programming

Levels of design:

| Type                               | Description                   |
| :--------------------------------- | :---------------------------- |
| naive Algorithms                   | Definition to algorithm, slow |
| Algorithm by way of standard tools | Standard techniques           |
| Optimized algorithm                | Improve existing algorithm    |
| Magic Algorithm                    | Unique insight                |


---

# Week3 - Greedy Algorthims

* http://dm.compsciclub.ru/app/quiz-largest-number
* http://dm.compsciclub.ru/app/quiz-car-fueling
* http://dm.compsciclub.ru/app/quiz-balls-in-boxes
* http://dm.compsciclub.ru/app/quiz-activity-selection

Main ingredients of greedy algorithm:

A move is called `safe` if there is an optimal solution consistent with this first move. So the general strategy is make a greedy choice, and prove that it is a safe move. 

* safe move
* prove safety 
* solve subproblem
* estimate running time 

## Grouping Children

Ways to group people in a certain manner
## Fractional Knapsack

How to bring k goods with you with capacity n
# Week 4 - Divide and conquer 

* http://dm.compsciclub.ru/app/quiz-opposite-colors

## Binary Search
## Polynomial Multiplication 

# Master theorem

If $T(N) = aT(\lceil\frac{n}{b}\rceil) + O(n^d)$ for constants $a>0, b>1, d \geq 0$ then:
$$
f(n) =
\begin{cases}
O(n^d) &\text{if } d > log_b a \\
O(n^d logn) &\text{if } d = log_b a\\
O(n^{log_b a}) &\text{if } d < log_b a
\end{cases}
$$

http://dm.compsciclub.ru/lti/local-maximum

# Dynamic

http://dm.compsciclub.ru/app/quiz-number-of-paths
http://dm.compsciclub.ru/app/quiz-take-the-last-stone
http://dm.compsciclub.ru/lti/three-rocks-game
http://dm.compsciclub.ru/app/quiz-primitive-calculator


