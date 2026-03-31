def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    return (x_num * n_den) == (n_num * x_den)
```
This function first extracts the numerator and denominator from both fractions using python's built-in `map` function to split on '/'. It then returns whether the product of the numerators divided by the product of the denominators is an integer.