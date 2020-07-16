def is_even(number):
    return True if number % 2 == 0 else False
   
   
   
def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(8) == True
    assert is_even(100) == True
    assert is_even(101) == False
    print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_is_even()