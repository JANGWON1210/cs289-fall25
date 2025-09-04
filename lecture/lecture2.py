import pandas as pd
import numpy as np

def pandas_example():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    df = pd.DataFrame(data)
    print("Pandas DataFrame:")
    print(df)

def numpy_example():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("NumPy Array:")
    print(arr)

if __name__ == "__main__":
    print("Hello, CS 289!")