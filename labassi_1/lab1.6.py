n = int (input("Enter number:"))
f1 = 0
f2 = 1
for i in range(2, n):
            f = f1 + f2
            f1 = f2
            f2 = f
print("The Fibonacchi number is:",f2)