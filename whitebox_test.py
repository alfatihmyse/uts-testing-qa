def calculate_area(base, height):
    if base <= 0 or height <= 0:
        return 0
    else:
        area = 0.5 * base * height
        return area

def white_box_test_calculate_area():
    # Test Case 1: Both base and height are positive
    area1 = calculate_area(5, 4)
    assert area1 == 10.0, "Test Case 1 Failed: Expected area is 10.0, but got {}".format(area1)

    # Test Case 2: Negative base
    area2 = calculate_area(-2, 3)
    assert area2 == 0, "Test Case 2 Failed: Expected area is 0, but got {}".format(area2)

    # Test Case 3: Negative height
    area3 = calculate_area(4, -5)
    assert area3 == 0, "Test Case 3 Failed: Expected area is 0, but got {}".format(area3)

    # Test Case 4: Negative base and height
    area4 = calculate_area(-3, -2)
    assert area4 == 0, "Test Case 4 Failed: Expected area is 0, but got {}".format(area4)

    # Test Case 5: Base is 0
    area5 = calculate_area(0, 6)
    assert area5 == 0, "Test Case 5 Failed: Expected area is 0, but got {}".format(area5)

    # Test Case 6: Height is 0
    area6 = calculate_area(7, 0)
    assert area6 == 0, "Test Case 6 Failed: Expected area is 0, but got {}".format(area6)

    # Test Case 7: Base and height are 0
    area7 = calculate_area(0, 0)
    assert area7 == 0, "Test Case 7 Failed: Expected area is 0, but got {}".format(area7)

if __name__ == '__main':
    white_box_test_calculate_area()
    print("White-box testing for calculate_area passed.")
