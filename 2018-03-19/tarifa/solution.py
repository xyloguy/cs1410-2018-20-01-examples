X = int(input())
N = int(input())

rollover = 0
for _ in range(N):
    P = int(input())
    rollover += X - P

print(rollover + X)

