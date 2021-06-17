m = {"a":1,"b":2,"c":3}
f = {"d":4,"e":5,"f":6}
mf = dict(m,**f)  # merging two dict
print(mf)
del m["c"] #deleting key
print(m)
a = [11,12,13,14]
b = ["ab","bc","cd","de"]
ab = dict(zip(b,a))  #merging two list to dict
print(ab)
sett = {1,2,3,4,5}
les = len(sett) # length of set
print(les)
x = {21,31,41,51,61,71}
y = {22,33,44,21,31,66}
x.difference_update(y) # deleting the intersection of set 2 from 1
print(x)