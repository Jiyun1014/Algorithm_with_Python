n = int(input())
confer = []
for i in range(n):
  a, b = map(int,input().split())
  confer.append([])
  confer[i].append(a)
  confer[i].append(b)

confer = sorted(confer, key=lambda x: (x[1],x[0]))
count = 0
secl = 1

for x in range(n):
  cnt = 1
  for y in range(secl,n):
    if confer[x][1] <= confer[y][0]:
      cnt += 1
      x=y
  if cnt > count:
    count = cnt
  secl += 1
    
print(count)