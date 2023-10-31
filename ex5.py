t = []

for i in range(0, 2):
    l = []
    for j in range(0, 2):
        n = int(input("Type number: "))
        l.append(n)
    t.append(l)

d=t[0][0]*t[1][1]-t[0][1]*t[1][0]
print("Determinant is :",d)