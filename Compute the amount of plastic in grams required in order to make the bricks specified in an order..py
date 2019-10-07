

def amount_of_plastic(width_brick, height_brick, length_brick, number_of_bricks):
    """Given the dimensions of a brick (width, height, length in cm) and the number of bricks ordered, calculate how much plastic, in grams, is required (if a cubic centimetre weighs 7 grams)."""
    
    # INSERT YOUR CODE BELOW THIS LINE FOR CALCULATING THE 
    # AMOUNT OF PLASTIC AND RETURNING THE RESULT (DO NOT CHANGE
    # THE HEADER OF THE FUNCTION WHICH HAS BEEN PROVIDED FOR YOU
    # ABOVE)
    Dimension = width_brick * height_brick * length_brick
    total_plastic_in_cm3 = Dimension * number_of_bricks
    amount_of_plastic_in_grams = total_plastic_in_cm3 * 7
    return amount_of_plastic_in_grams


# DO NOT CHANGE THE CODE BELOW THIS LINE
# The code below automatically tests your function
# following the approach described in 
# Block 2 Part 4 (Page 207 and further).
# Before making any changes to this file, 
# when you run it, you will get an AssertionError. 
# Once you have completed the file with correct
# code, the AssertionError should no longer appear and
# "tests passed" will appear in the shell.


def test_amount_of_plastic():
    """Test the amount_of_plastic() function."""
    # Test for brick with dimensions 0, 0, 0 and 
    # order of 20 bricks
    assert amount_of_plastic(0, 0, 0, 20) == 0
    
    # Test for brick with dimensions 1, 1, 1 and 
    # order of 0 bricks
    assert amount_of_plastic(1, 1, 1, 0) == 0

    # Test for brick with dimensions 1, 1, 1 and 
    # order of 20 bricks
    assert amount_of_plastic(1, 1, 1, 20) == 140
    
    # Test for brick with dimensions 1, 2, 3 and 
    # order of 100 bricks
    assert amount_of_plastic(1, 2, 3, 100) == 4200
    
    print ("tests passed") 
 
 
test_amount_of_plastic()
    