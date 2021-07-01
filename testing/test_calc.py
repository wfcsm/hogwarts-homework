
# 被测方法
def add(a,b):
    return a+b

# 测试方法
def test_add1():
    print("1+1 ==2")
    assert 2 == add(1,1)

def test_add2():
    print("300 == add(100,200)")
    assert 300 == add(1,200)

def test_add3():
    print("300 == add(100,200)")
    assert 300 == add(3,200)

def test_add4():
    print("300 == add(100,200)")
    assert 300 == add(100,200)