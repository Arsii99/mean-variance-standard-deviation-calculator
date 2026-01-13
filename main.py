import mean_var_std
from test_module import *

# Test the calculate function
if __name__ == '__main__':
    # Example test
    result = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
    print("Result:")
    print(result)
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main()
