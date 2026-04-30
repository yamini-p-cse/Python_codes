import numpy as np

# Creating array object

arr = np.array([[1, 2, 3],

                [4, 2, 5]])

# Printing type of arr object

print("Array is of type: ", type(arr))

# Printing array dimensions (axes)

print("No. of dimensions: ", arr.ndim)

# Printing shape of array

print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array

print("Size of array: ", arr.size)

# Printing type of elements in array

print("Array stores elements of type: ", arr.dtype)

#numpy_in_array_concept

import numpy as np

# Creating array from list with type float

a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')

print ("Array created using passed list:\n", a)

# Creating array from tuple

b = np.array((1 , 3, 2))

print ("\nArray created using passed tuple:\n", b)
#numpy_2d_array_concept
import numpy as np

# Creating a 2D array

arr = np.array([[1, 2, 3],

                [4, 5, 6],

                [7, 8, 9]])

# Print the original array

print("Original array:")

print(arr)

# Indexing a single element

print("\nElement at row 1, column 2:")

print(arr[1, 2])

#numpy_operations_concept

import numpy as np

# Create a 1D array

arr = np.array([1, 2, 3, 4, 5])

# Add 10 to each element

arr_add = arr + 10

# Multiply each element by 2

arr_mul = arr * 2

# Print the results

print("Original array:", arr)

print("Array after adding 10:", arr_add)

# pandas_series_concept
import pandas as pd

# Create a Pandas Series
data = [1, 2, 3, 4, 5]
series = pd.Series(data)

print("Pandas Series:")
print(series)

# Create a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

# pandas_dataframe_creation_concept

import pandas as pd

# Create a Pandas Series

data = [1, 2, 3, 4, 5]

series = pd.Series(data)

# Create a Pandas DataFrame

data = {

    'Name': ['Alice', 'Bob', 'Charlie'],

    'Age': [24, 27, 22]

}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")

print(df)
# pandas_row_selection_concept

import pandas as pd

# Sample data

data = {

    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],

    'Age': [24, 27, 22, 32, 29],

    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

}

# Creating DataFrame

df = pd.DataFrame(data)

# Selecting multiple rows by index

print("\nSelecting rows with index 1 and 3:")

print(df.iloc[[1, 3]])


# pandas_missing_data_handling_concept
import pandas as pd

import numpy as np

# Sample data with missing values

data = {

    'A': [1, 2, np.nan, 4, 5],

    'B': [np.nan, 10, 20, np.nan, 50],

    'C': ['foo', 'bar', 'baz', 'qux', 'quux']

}

df = pd.DataFrame(data)

# Display the DataFrame with missing values

print("Original DataFrame:")

print(df)

# Fill missing values with a specific value, e.g., 0

df_filled = df.fillna(0)

# Display the DataFrame after filling missing values

print("\nDataFrame after filling missing values with 0:")

print(df_filled)

# pandas_merging_data_concept
import pandas as pd

# Creating two small DataFrames

df1 = pd.DataFrame({

    'key': ['A', 'B', 'C', 'D'],

    'value1': [1, 2, 3, 4]

})

df2 = pd.DataFrame({

    'key': ['B', 'D', 'E', 'F'],

    'value2': ['foo', 'bar', 'baz', 'qux']

})

# Performing an inner join on 'key'

inner_join = pd.merge(df1, df2, on='key', how='inner')

print("Inner Join:")

print(inner_join)

# Performing a left join on 'key'

left_join = pd.merge(df1, df2, on='key', how='left')

print("\nLeft Join:")

print(left_join)
# pandas_data_visualization_concept
import pandas as pd

import matplotlib.pyplot as plt

# Create a sample DataFrame

data = {

    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],

    'Age': [24, 27, 22, 32, 29],

    'Score': [85, 72, 88, 95, 78]

}

df = pd.DataFrame(data)

# Plotting a bar chart

df.plot(kind='bar', x='Name', y='Score', legend=None)

plt.xlabel('Name')

plt.ylabel('Score')

plt.title('Student Scores')

plt.show()

