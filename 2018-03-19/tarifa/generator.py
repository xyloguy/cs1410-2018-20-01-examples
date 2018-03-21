import random

X = random.randint(1, 100)
print(X)
N = random.randint(1, 100)
print(N)

allowed = X
for _ in range(N):
    P = random.randint(0, allowed)
    print(P)
    allowed += X - P
