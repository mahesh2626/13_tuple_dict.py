"""tuple"""
# print(dir(tuple))
a=(65,64,'hi','hello',25,25)
print(a.count(4))
print(a.count('hi'))
print(a.count(25))
print(a.count(65))
'''index'''
a=(65,64,'hi','hello',1,25)
print(a.index(64))
print(a.index(25))
print(a.index('hello'))
print(a.index(65))

"""dict"""
# print(dir(dict))
a={2:5,5:'hi',6:8}
print(type(a))
a.clear()
print(a)
"""copy"""
a={2:5,5:'hi',6:8}
b=a.copy()
print(b)
"""fromkeys"""
a=[1,2,3]
print(dict.fromkeys(a,5))
x=[5,'hi',65]
print(dict.fromkeys(x,'hello'))
"""get"""
a={2:5,5:'hi',6:8}
print(a.get(5))
print(a.get(2))
print(a)
print(a.get('hi'))
"""items"""
a={2:5,5:'hi',6:8}
print(a.items())
a.items
"""keys"""
a={2:5,5:'hi',6:8}
print(a.keys())
a={6:54,'hi':65,1:3}
print(a.keys())
"""pop"""
a={2:5,5:'hi',6:8}
a.pop(5)
print(a)
a.pop(6)
print(a)
"""pop items"""
a={2:5,5:'hi',6:8,9:2}
a.popitem()
print(a)
a={2:5,5:'hi',6:8}
print(a.popitem())
a.popitem()
print(a)
"""setdefault"""
a={2:5,5:'hi',6:8}
print(a.setdefault(2))
print(a)
a.setdefault(9,1)
print(a)
"""values"""
a={2:5,5:'hi',6:8}
a.values()
print(a.values())
x={1:2,3:4,5:6}
print(x.values())