
math_l=list()
names=list()
subnames=list()
geom=list()
tiers=list()

t8=list()
t9=list()
t10=list()
t11=list()



f=open('mat_dv.txt','r')
for i in f:
    s=i
    l=i.split()
    math=int((i.split(' ')[3]))
    math_l.append(math)

    geo=int((i.split(' ')[4]))
    geom.append(geo)

    name=str(i.split(' ')[0])
    line=name.strip()
    names.append(line)

    subname=str(i.split(' ')[1])
    line2=subname.strip()
    subnames.append(line2)

    tier=int(i.split(' ')[2])
    tiers.append(tier)


max=math_l[0]
pos=0
for i in range(len(math_l)):
    if math_l[i]>max: max=math_l[i];pos=i
print('Алгебра: ',names[pos],' ',subnames[pos],' ',tiers[pos])


max=geom[0]
pos2=0
for i in range(len(geom)):
    if geom[i]>max: max=geom[i];pos2=i
print('Геометрия: ',names[pos2],' ',subnames[pos2],' ',tiers[pos2])

