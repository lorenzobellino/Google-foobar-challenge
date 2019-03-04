x=[5,6,45,67,89,40,91,32,59]
y=[5,6,45,67,89,91,40,59,32,87,95,4,65,565]
sumx=0
sumy=0
for i in x:
    sumx=sumx+i

for j in y:
    sumy=sumy+j


print(sum(x))
print(sumx)
print(sum(y))
print(sumy)

if len(x)>len(y):
    risultato=sumx-sumy

else:
    risultato=sumy-sumx

print(risultato)
