from um import count

def main():
    test_cases()
    test_word()
    test_space()

def test_cases():
    assert count("um?") == 1
    assert count("Um") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album") == 1
    
def test_word():
    assert count("yummi") == 0
       
def test_space():
    assert count("hello um world") == 1
    assert count("um.") == 1

if __name__ == "__main__":
    main()