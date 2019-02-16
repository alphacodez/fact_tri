print("Make sure it is a trinomial")
first = float(input("Enter first term: "))
second = float(input("Enter second term:"))
third = float(input("Enter third term: "))
i = 0
q = 0
run = 0
f = []
s = []
t = []
n = []
m = []


def tri(place, pla):
    for n in range(-500, 500):
        for num in range(-500, 500):
            #print("number", n, num, n*num)
            if n * num == place:
                pla.append([n, num])


tri(first, f)
#tri(second, s)
tri(third, t)
'''
for num in range(len(f)):
    while run <= num:
        n.append(f[i][q])
        #i += 1
        q += 1
        if q > 1:
            q = 0
            i += 1
            run += 1
q = 0
i = 0
run = 0
for num in range(len(t)):
    while run <= num:
        m.append(t[i][q])
        #i += 1
        q += 1
        if q > 1:
            q = 0
            i += 1
            run += 1
''''''
q = 0
i = 0
run = 0
c = 0
v = 0
while 1 == 1:
    print("Loop", q, i, c, v)
    if (n[q] * m[i]) + (n[c] * m[v]) == second:
        #print(n[q], m[i], n[c], m[v])
        print(n[q])
        print(m[i])
        print(n[c])
        print(m[v])
        print("Right", n[q], m[i], n[c], m[v])
        break
    try:
        q -= 1
        i -= 2
        c -= 3
        v -= 4
        print("Added", q, i, c, v)
    except IndexError:
        q = 0
        i = 0
        c = 0
        v = 0
        print("Neato ", q, i, c, v)
'''
print(f)
#print(s)
print(t)
'''print(n)
print(m)
print(q)
print(i)
print(c)
print(v)'''
