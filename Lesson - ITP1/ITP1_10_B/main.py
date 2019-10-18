import math
a, b, C = map(int, input().split())
sinc = math.sin(math.radians(C))
cosc = math.cos(math.radians(C))
S = 0.5 * a * b * sinc
L = a + b + math.sqrt((a ** 2) + (b ** 2) - (2 * a * b * cosc))
h = b * sinc
print(S, L, h, sep='\r\n')
