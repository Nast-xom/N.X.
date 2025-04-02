k = 0
x=int(input())
while x!=0:
    if (x<10)and(x%3==0):
        k += 1
    x=int(input())
print(k)