import main
def test_is_factor1():
    if main.is_factor1(3, 12) == 4:
        print("Test is_factor1(a, b) is OK")
        print()
    else:
        print("Test is_factor1(a, b) is Fail")
        print()
def test_is_factor2():
    if main.is_factor2(5, 12) == 'False':
        print("Test is_factor2(a, b) is OK")
        print()
    else:
        print("Test is_factor2(a, b) is Fail")
        print()
def test_is_factor3():
    if main.is_factor3(7, 14) == 2:
        print("Test is_factor3(a, b) is OK")
        print()
    else:
        print("Test is_factor3(a, b) is Fail")
        print()
def test_is_factor4():
    if main.is_factor4(2, 14) == 7:
        print("Test is_factor4(a, b) is OK")
        print()
    else:
        print("Test is_factor4(a, b) is Fail")
        print()
def test_is_factor5():
    if main.is_factor5(7, 15) == 'False':
        print("Test is_factor5(a, b) is OK")
        print()
    else:
        print("Test is_factor5(a, b) is Fail")
        print()

def test_is_multiple1():
    if main.is_multiple1(12, 3) == 4:
        print("Test is_multiple1(a, b) is OK")
        print()
    else:
        print("Test is_multiple1(a, b) is Fail")
        print()
def test_is_multiple2():
    if main.is_multiple2(12, 5) == 'False':
        print("Test is_multiple2(a, b) is OK")
        print()
    else:
        print("Test is_multiple2(a, b) is Fail")
        print()
def test_is_multiple3():
    if main.is_multiple3(12, 4) == 3:
        print("Test is_multiple3(a, b) is OK")
        print()
    else:
        print("Test is_multiple3(a, b) is Fail")
        print()
def test_is_multiple4():
    if main.is_multiple4(12, 6) == 2:
        print("Test is_multiple4(a, b) is OK")
        print()
    else:
        print("Test is_multiple4(a, b) is Fail")
        print()
def test_is_multiple5():
    if main.is_multiple5(12, 7) == 'False':
        print("Test is_multiple5(a, b) is OK")
        print()
    else:
        print("Test is_multiple5(a, b) is Fail")
        print()

def test_num_digits():
    if main.num_digits(143) == 3:
        print("Test num_digits(a, b) is OK")
        print()
    else:
        print("Test is_multiple5(a, b) is Fail")
        print()


test_is_factor1()
test_is_factor2()
test_is_factor3()
test_is_factor4()
test_is_factor5()

test_is_multiple1()
test_is_multiple2()
test_is_multiple3()
test_is_multiple4()
test_is_multiple5()
