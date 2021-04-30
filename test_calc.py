import unittest
import calc


def test_addition(num1, num2):
    print("Doing correct tests for addition.\n")
    try:
        unittest.assertEqual(calc.addition(1,2), 3)
    except AssertionError as msg:
        print(msg)
    try:
        unittest.assertEqual(calc.addition(992,2), 994)
    except AssertionError as msg:
        print(msg)
    print("This next test should cause an error.")
    try:
        unittest.assertEqual(calc.addition(22,5),28)
    except AssertionError as msg:
        print(msg)
    print("Testing user inputted numbers.")
    try:
        unittest.assertEqual(calc.addition(num1, num2),num1+num2)
    except AssertionError as msg:
        print(msg)
    print("\n")
        

def test_subtraction(num1, num2):
    print("Doing correct tests for subtraction.\n")
    try:
        unittest.assertEqual(calc.subtraction(9,3),6)
    except AssertionError as msg:
        print(msg)
    try:
        unittest.assertEqual(calc.subtraction(1000,3),997)
    except AssertionError as msg:
        print(msg)
    print("This next test should cause an error.")
    try:
        unittest.assertEqual(calc.subtraction(81,3),77)
    except AssertionError as msg:
        print(msg)
    print("Testing user inputted numbers.")
    try:
        unittest.assertEqual(calc.subtraction(num1, num2),num1-num2)
    except AssertionError as msg:
        print(msg)
    print("\n")




def test_multiplication(num1, num2):
    print("Doing correct tests for multiplication.\n")
    try:
        unittest.assertEqual(calc.multiplication(9,3),27)
    except AssertionError as msg:
        print(msg)
    try:
        unittest.assertEqual(calc.multiplication(23,3),69)
    except AssertionError as msg:
        print(msg)
    print("This next test should cause an error.")
    try:
        unittest.assertEqual(calc.multiplication(13,5),82)
    except AssertionError as msg:
        print(msg)
    print("Testing user inputted numbers.")
    try:
        unittest.assertEqual(calc.multiplication(num1, num2),num1*num2)
    except AssertionError as msg:
        print(msg)
    print("\n")




def test_division(num1, num2):
    print("Doing correct tests for division.\n")
    try:
        unittest.assertEqual(calc.division(9,3),3)
    except AssertionError as msg:
        print(msg)
    try:
        unittest.assertEqual(calc.division(36,6),6)
    except AssertionError as msg:
        print(msg)
    print("This next test should cause an error.")
    try:
        unittest.assertEqual(calc.division(13,2),7)
    except AssertionError as msg:
        print(msg)
    print("Testing user inputted numbers.")
    try:
        unittest.assertEqual(calc.division(num1, num2),num1/num2)
    except AssertionError as msg:
        print(msg)
    print("\n")





def main():
    int1 = int(input("Enter one number for testing. "))
    int2 = int(input("Enter another number for testing. "))
    test_addition(int1, int2)
    test_subtraction(int1, int2)
    test_multiplication(int1, int2)
    test_division(int1, int2)


if __name__ == "__main__":
    main()