
import math

b = int(input('What walue is side b: '))

c = int(input('What walue is side c: '))

A_deg = int(input('What walue is angle A in degrees: '))

A = A_deg * (3.142 / 180.0)

a_squared = (b * b) + (c * c) -2 * b * c *math.cos(A)

a = math.sqrt(a_squared)

print('The walue of the side a is %0.1f'%a)