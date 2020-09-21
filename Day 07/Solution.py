n=int(input())
l=list(map(int,input().split(" ")))
l.reverse()
for i in range(n):
    print(l[i],end=" ")
