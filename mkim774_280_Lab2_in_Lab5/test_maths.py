import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        # Arrange & Act
        result = maths.add(3,4)
        # Assert
        self.assertEqual(result, 7, "The add function returned an incorrect value.")
        
    def test_add_with_no_base_parameter(self):
        ''' Tests the add function with no base parameter given '''
        # Arrange & Act
        result = maths.add(5,5)
        # Assert
        self.assertEqual(result, 10, "The add function returned an incorrect value.")

    def test_add_with_base_ten(self):
        ''' Tests the add function with the optional base parameter given, which is ten '''
        # Arrange & Act
        result = maths.add(5,5,10)
        # Assert
        self.assertEqual(result, '10', "The add function returned an incorrect value.")

    def test_add_with_base_under_ten(self):
        ''' Tests the add function with the optional base parameter given, which is under ten '''
        # Arrange & Act
        result = maths.add(5,5,7)
        # Assert
        self.assertEqual(result, '13', "The add function returned an incorrect value.")
    
    def test_add_with_base_over_ten(self):
        ''' Tests the add function with the optional base parameter given, which is over ten '''
        # Arrange & Act
        result = maths.add(5,5,12)
        # Assert
        self.assertEqual(result, 'A', "The add function returned an incorrect value.")

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        # Arrange & Act
        result = maths.fibonacci(5)
        # Assert
        self.assertEqual(result, 5, "The fibonacci function returned an incorrect value.")

    def test_convert_base_under_ten(self):
        ''' Tests the convert_base function with base under 10 '''
        # Arrange & Act
        result = maths.convert_base(23, 9)
        # Assert
        self.assertEqual(result, '25', "The convert_base function returned an incorrect value.")
    
    def test_convert_base_ten(self):
        ''' Tests the convert_base function with base 10 '''
        # Arrange & Act
        result = maths.convert_base(23, 10)
        # Assert
        self.assertEqual(result, '23', "The convert_base function returned an incorrect value.")
    
    def test_convert_base_over_ten(self):
        ''' Tests the convert_base function with base over 10 '''
        # Arrange & Act
        result = maths.convert_base(23, 13)
        # Assert
        self.assertEqual(result, '1A', "The convert_base function returned an incorrect value.")

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
