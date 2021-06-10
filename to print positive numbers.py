L=[]
for i in range(0,5):
    n=int(input("enter the number"))
    L.append(n)
print("List before removing",L)
for num in L:
    if num < 0:
        L.pop(L.index(num))
print("List after removing",L)
