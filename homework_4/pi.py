# Вычислить число Пи c заданной точностью d
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

def calc_PI(value):
  n=2
  pi = 4*[1,-1/3]
  count = 1
  while count>value:
    pi.append(4*(-1)**n/(2*n+1))
    count = abs(sum(pi[:-1]) - sum(pi[:-2]))
    n +=1
  return math.floor(sum(pi)*int(1/value))*value

d = 0.001
print(calc_PI(d))