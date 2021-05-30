# リスト内包表記

t = {1,2,3,4,5}
t2 = {5,6,7,8,9,10}

# 普通にfor文を利用して記載
r = []
for i in t:
    if i%2 == 0:
        r.append(i)
print(r)

# リスト内包表記を利用して記載
r = [i for i in t]
print(r)

# リスト内包表記を利用して記載
r = [i for i in t if i%2==0]
print(r)

# ネストありの記載
r=[]
for i in t:
    for j in t2:
        r.append(i*j)

print(r)

# ネストがある際のリスト内包表記の記載
r = [i*j for i in t for j in t2]
print(r)
