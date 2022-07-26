n = int(input())

i=-1
L=[]

for _ in range(n):
    numbers = list(map(int,input().split()))
    L.append([item + numbers[i] for item in numbers])
    i-=1
print(L)
