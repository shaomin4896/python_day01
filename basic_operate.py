a = int(input("第1 個邊"))
b = int(input("第2 個邊"))
c = int(input("第3 個邊"))
print(a,b,c)
A = 0
s = (a + b + c) / 2
A = (s * (s - a) * (s - b) * (s -c)) ** 0.5
print(A)