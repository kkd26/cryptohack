#!/usr/bin/python3

def modexp(g, e, m):
  a = g % m
  b = 1
  while (e > 0):
    if(e % 2 == 1):
      b = b * a % m
    a = a * a % m
    e = e // 2
  return b
