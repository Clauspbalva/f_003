"""
f_003.py | Claus Pagano | Last update: 2022-8-17

Algorithms and Data Structures practice with Python

"""


# --------------------------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------------------------

from f_000 import function_test


# --------------------------------------------------------------------------------------------------
# FUNCTION DECLARATION 
# --------------------------------------------------------------------------------------------------

def multiply(n1, n2):
    """
        Description: returns the multiplication of n1 and n2 by successive addition

        Parameters:
            n1 (int): number 1
            n2 (int): number 2
        
        Return:
            n1 * n2
    """

    # Validates parameters: integer type
    if type(n1) != int or type(n2) != int:
        return None

    # Determines result sign
    if (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
        sign = 1
    else:
        sign = -1
    n1 = abs(n1)
    n2 = abs(n2)

    # Successive addition: performs n1 times the addition n2 + n2
    m = 0
    if n1 != 0 or n2 != 0:
        while(n1 >= 1):
            m += n2
            n1 -= 1
    return sign * m


# --------------------------------------------------------------------------------------------------
# TESTING
# --------------------------------------------------------------------------------------------------

# Dictionary with test cases
test_config = {
    'function': multiply,
    'input_names': ['n1', 'n2'],
    'tests': [
        {'id': 1, 'input_values': [1.2, 0], 'output_expected': None},
        {'id': 2, 'input_values': [1, '12'], 'output_expected': None},
        {'id': 3, 'input_values': [0, 0], 'output_expected': 0},
        {'id': 4, 'input_values': [0, 1], 'output_expected': 0},
        {'id': 5, 'input_values': [0, -1], 'output_expected': 0},
        {'id': 6, 'input_values': [-1, 0], 'output_expected': -0},
        {'id': 7, 'input_values': [-2, -8], 'output_expected': 16}
    ],
    'print_details': True  
}


# --------------------------------------------------------------------------------------------------
# MAIN PROCEDURE
# --------------------------------------------------------------------------------------------------

if __name__ == "__main__":   
    function_test(test_config)



