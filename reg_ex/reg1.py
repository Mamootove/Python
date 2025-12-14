import re

text = "54845"

res = re.search(r"\s", text)

print(re.sub(r"4", r"2", text))


name = "Rozhin"

print(name)
last_name = "Hesadi"

kalamat = f"{name} {last_name}"
l= [kalame for kalame in kalamat]
l.remove(' ')


l_k = kalamat.split()


print(l_k)
l_khafan = []

for esm in l_k:
    l_khafan.append([j for j in esm])
    
print(l_khafan)



dic = {}

zipper = zip(l_khafan[0], l_khafan[1])
print(list(zipper))
c = 0
for k in list(zipper):
    c += 1
    
    
for k in list(zipper):
    print(k[0])

