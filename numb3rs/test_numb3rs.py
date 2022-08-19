from numb3rs import validate

def main():
   test_validate1()
   test_validate2()
   test_validate3()
   test_validate4()
   test_validate5()
    

def test_validate1():
    assert validate(r"127.0.0.1") == True
    
def test_validate2():
    assert validate(r"255.255.255.255") == True
    
def test_validate3():
    assert validate(r"512.512.512.512") == False
    
def test_validate4():
    assert validate(r"1.2.3.1000") == False
    
def test_validate5():
    assert validate(r"cat")== False
    
    
if __name__ == "__main__":
    main()
