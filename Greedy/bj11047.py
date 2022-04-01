n, k = map(int, input().split())
coins = []

for i in range(n):
  a = int(input())
  coins.append(a)

coins.sort(reverse = True)
count = 0

for j in coins:
  count += k//j
  k %= j
  
print(count)