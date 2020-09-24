# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for num in range(n):
    i=int(input())
    
    for j in range(2,int(i**(1/2))+1):
        if i%j==0:
            print("Not prime")
            break
    else:
        if i==1:
            print("Not prime")
        else:
            print("Prime")
