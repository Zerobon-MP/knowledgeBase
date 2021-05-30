# 名前空間とスコープ

"""
Test Test #####################
"""

animal = 'cat'

def f():
    global animal
    animal = 'dog'
    print('local:', animal)

f()
print('global:', animal)

print('########################')

animal2 = 'cat'

def f2():
    animal2 = 'dog'
    print('local:', locals())

f2()
print('global:', globals())

print('@@@@@@@@@@@@@@@@@@@@@@@@@')

def f3():
    """Test func doc"""
    print(f3.__name__)
    print(f3.__doc__)

f3()
print('global:', globals())