#!/usr/bin/python3

class NonInvertable(Exception):
  def __init__(self, message="The modulus inverse doesn't exist"):
    self.message = message
    super().__init__(self.message)

def modinv(a, b):
  (x, y, z, w) = (0, 1, 1, 0)
  b0 = b
  while (True):
    if (a % b == 0):
      if (b == 1):
        if (x < 0):
          x += b0
        return x
      else:
        raise NonInvertable
    q = a//b
    (a, b, x, z) = (b, a % b, z - q*x, x)
