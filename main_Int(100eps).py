︠from sympy import Symbol
from sage.symbolic.integration.integral import definite_integral
t = Symbol('t')
def integral1(eps):
    return definite_integral(100*(eps*(1-x) * (x-(1+(2-eps)*t)/4) 
                             * ((x - (1+3*(2-eps)*t))/4)**2),
                             x, ((1+ (2-eps)*t)/4),((1+2*t)/4))

def integral2(eps):
    return definite_integral(((-16/(2*t+1)**2)*((4*x**2)/(2*t+1) - abs(x) +2)
                              + 32/((2*t+1)**2)
                              + 64/((2*t+1)**3) - 16 * abs(x)/((2*t+1)**2)
                              + 100*(eps*(1-x) * (x-(1+(2-eps)*t)/4) 
                              * ((x - (1+3*(2-eps)*t))/4)**2))**2, x,(((1+2*t)/4)), 1)

def rezult(eps):
    a = integral1(eps)
    b = integral2(eps)
    c = definite_integral(a+b, t, 0.5, 1)
    return sqrt(2*c)

nums = [0.5, 0.35, 0.25, 0.15, 0.05, 0.001]
for num in nums:
    print(rezult(num))









