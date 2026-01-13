import numpy as np


def calculate(lst):
    """
    Calculate mean, variance, standard deviation, max, min, and sum
    along rows, columns, and flattened matrix for a 3x3 matrix.
    
    Args:
        lst: A list containing 9 digits
        
    Returns:
        A dictionary with statistics for axis 0 (rows), axis 1 (columns), and flattened matrix
        
    Raises:
        ValueError: If the list doesn't contain exactly 9 elements
    """
    # Check if list has 9 elements
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 numpy array
    arr = np.array(lst).reshape(3, 3)
    
    # Calculate statistics along axis 0 (rows), axis 1 (columns), and flattened
    result = {
        'mean': [
            np.mean(arr, axis=0).tolist(),  # axis 0 (rows)
            np.mean(arr, axis=1).tolist(),  # axis 1 (columns)
            float(np.mean(arr))              # flattened
        ],
        'variance': [
            np.var(arr, axis=0).tolist(),   # axis 0 (rows)
            np.var(arr, axis=1).tolist(),   # axis 1 (columns)
            float(np.var(arr))              # flattened
        ],
        'standard deviation': [
            np.std(arr, axis=0).tolist(),   # axis 0 (rows)
            np.std(arr, axis=1).tolist(),   # axis 1 (columns)
            float(np.std(arr))              # flattened
        ],
        'max': [
            np.max(arr, axis=0).tolist(),   # axis 0 (rows)
            np.max(arr, axis=1).tolist(),   # axis 1 (columns)
            int(np.max(arr))                # flattened
        ],
        'min': [
            np.min(arr, axis=0).tolist(),   # axis 0 (rows)
            np.min(arr, axis=1).tolist(),   # axis 1 (columns)
            int(np.min(arr))                # flattened
        ],
        'sum': [
            np.sum(arr, axis=0).tolist(),   # axis 0 (rows)
            np.sum(arr, axis=1).tolist(),   # axis 1 (columns)
            int(np.sum(arr))                # flattened
        ]
    }
    
    return result
