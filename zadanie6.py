a=0
e=0
o=0
u=0
i=0
print('Введите слово: ')
word=input()
for j in range(0,len(word)):
    x=word[j]
    if x=='a':
        a+=1
    if x=='e':
        e+=1
    if x=='o':
        o+=1
    if x=='u':
        u+=1
    if x=='i':
        i+=1
if a==0:
    a=False
if e==0:
    e=False
if o==0:
    o=False
if e==0:
    e=False
if u==0:
    u=False
if i==0:
    i=False

print('a=',a,'o=',o,'u=',u,'e=',e,'i=',i)