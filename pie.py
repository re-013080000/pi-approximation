#pi approximation with Monte-Carlo algorithm

import random as r
import time as t

Try = 1

def main(Try):
  print(f"try n°{Try}")
  p = int(input("default(10^6) | précision: "))
  def pi(n):
    In = 0
    Tot = 0
    for z in range(n):
      x = round(r.uniform(0.00, 2.00), 2) - 1
      y = round(r.uniform(0.00, 2.00), 2) - 1
      if (x**2+y**2)**0.5 < 1:
        In += 1
      Tot += 1
    pi = In/Tot
    return 4*pi
  pie = pi(p)
  print(f'•π approximation:   {pie}')
  print("")
  t.sleep(2)

while True:
  main(Try)
  Try += 1
