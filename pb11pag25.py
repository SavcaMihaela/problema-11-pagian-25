n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,'elemente pentru vectorul creat')
for i in range(0, n):
    x=int(input('Dati elementul='))
    a.extend([x])
print(a)
print('b) afiseaza pe ecran numerele in ordinea inversa a introducerii in calculator')
for b in reversed (a):
    print(b, end = '')
print ('c) sorteaza componentele tabloului in ordine descrescatoare')
c=sorted(a)
c.sort(reverse=True)
print(c)
print('d) afiseaza pe ecran doar componentele pare')
d=[]
for d in a:
    if d%2==0:
    print(d, end = '')
print('e) afiseaza pe ecran media aritmetica a componentelor pare')
print(sum(d)/len(d))
print ('f) afiseaza pe ecran doar componentele impare')
f=[]
for f in a:
    if f%2!=0:
        print(f, end = '')
print('g) componentele care sunt mai mari ca x si nu sunt divizibili cu y')
x=eval(input('Introduceti x:'))
y=eval(input('Introduceti y:'))
g=[]
for i in a:
    if i>x and i%y !=0:
        g.append(i)
        print(g, end = '')
print('h) componentele care sunt mai mari ca x si mai mici de cat y')
h=[]
for i in a:
    if i>%x and i<y :
        h.append(i)
        print(i, end = '')
        print(h)
##print('i)afiseaza pe ecran pozitiile componentelor imparee negative
##i=[]
##print('j)afiseaza pe ecran pozitiile componentelor ce contin doar doua cifre semnificative
##j=[]
print(f'k) prima componenta a tabloului inlocuita cu componenta de valoare minima din tabloul respectiv')
a[0]=min(a)
print(a)
print(f'l)componenta de valoare minima din tabloul respectiv inlocuita cu prima componenta a acestuai')
a.[a.index(min(a))]=[0]
print(a)
print('m)creaza un tablou nou, format doar din componente pare ale tabloului introdus de la tastatura')
m=[]
a=list(filter(lambda x:(x/2==0),a))
print('m=', a)
print('n) creaza un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatura')
n=[]
a=list(filter(lambda x: (x%3==0),a))
print('n=', a)
