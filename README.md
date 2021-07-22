# MetodeNewton-Raphson 
is a method of finding the root of a function f(x) with a one-point approach, where the function f(x) has a derivative. This method uses a one-point approach as a starting point. The closer our chosen starting point is to the real root, the faster it will converge to the root.
more information about [newtonrapshon](https://en.wikipedia.org/wiki/Newton%27s_method)

# algorithm
1. Start
2. Define the function as f(x)
3. Define the first derivative of f (x) g (x) g (x) i (x)
4. Enter the first number, coefficient x, constant, initial estimate (top), tolerable error (error)
   and maximum iterations (bottom)
5. Initialization of iteration counter i = 1
6. If g (top) = 0 then print "Error"
   and go (12) otherwise go (7)
7. Calcualte x1 = up - f (above) / add (above) for addition and calcualte x1 = up - f(above)/less(above) for subtraction
8. Iteration counter increment i = i + 1
9. If i>=N then print "not convergent"
   and go (12) otherwise go (10)
10. If | f(x1) | > e then set up = x1
    and go (6) otherwise go (11)
11. Print the result as x1
12. Stop

# pseudocode
1. Start
2. Define the function as f(x)
3. Define the derivative of the function as g(x)
4. Input:
A. Initial guess over
b. Error Tolerable error
c. Bottom Maximum Iteration
5. Initialization of iteration counter step = 1
6. Do it
If bottom(up) = 0
Print "error"
Stop
Ends if
if operator +
x1 = up - f (up)/plus(up)
  top = x1
if operator -
x1 = up - h(up)/less(up)

step = step + 1

If step> down
Print "Not Converging"
Stop
Ends if
   While abs f(x1)> e
7. Print root as x1
8. Stop
"""
