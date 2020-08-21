n = int(input("Please enter a number :"))

num = [int(i) for i in str(n)]

b = []

while len(num)> 1:
    a = sum(num)
    num = [int(x) for x in str(a)]



if sum(num) == 1:
    print(f"{n} is a magic number")
else :
    print(f"{n} is not a magic number")
    


    
