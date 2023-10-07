import pandas as pd

# List of source file names
file_names = ["source1.txt", "source2.txt", "source3.txt", "source4.txt", "source5.txt"]

# Initialize an empty list to store dataframes from each source file
dfs = []

# Read data from each source file and store it as a dataframe with labeled columns
for i, file_name in enumerate(file_names, start=1):
    df = pd.read_csv(file_name, header=None)
    df.columns = [f'Source {i}']
    dfs.append(df)

# Concatenate dataframes horizontally to create the combined matrix
combined_matrix = pd.concat(dfs, axis=1)

# Label the index (rows) as "Page 1" to "Page 10000"
combined_matrix.index = [f'Page {i}' for i in range(1, 10001)]

# Calculate the sum of each row and add it as a new column "Source Sum"
combined_matrix['Source Sum'] = combined_matrix.sum(axis=1)

# Save the combined matrix to a new TSV (text) file
combined_matrix.to_csv("combined_matrix.txt", sep='\t')

sorted_matrix = combined_matrix.sort_values(by='Source Sum', kind='quicksort')

# Display the sorted matrix
print("Sorted Matrix by Page Sum (Least to Most):")
print(sorted_matrix)

sorted_matrix.to_csv("combined_matrix.txt", sep='\t')

# Optimized inversion counting
def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])
    merged, split_inv = merge_and_count(left, right)

    return merged, left_inv + right_inv + split_inv

def merge_and_count(left, right):
    merged = []
    inversions = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions

# Create a dictionary to store the number of inversions for each source
inversions_count = {}

# Iterate through each source column and calculate the inversions using the optimized method
for i in range(1, 6):
    source_name = f'Source {i}'
    _, inversions = count_inversions(list(sorted_matrix[source_name]))
    inversions_count[source_name] = inversions

# Print the number of inversions for each source
for source_name, inversions in inversions_count.items():
    print(f"{source_name} has {inversions} inversions")
    

#use insertionsort to sort the inversions from least to greatest
def insertion_sort(inversions_list):
    for i in range(1, len(inversions_list)):
        key = inversions_list[i]
        j = i - 1
        while j >= 0 and key[1] < inversions_list[j][1]:
            inversions_list[j + 1] = inversions_list[j]
            j -= 1
        inversions_list[j + 1] = key

# Create a list of tuples containing source names and their inversions
inversions_list = list(inversions_count.items())

# Sort the list of inversions from least to greatest using insertion sort
insertion_sort(inversions_list)

# Display the sorted inversions
print()
print("Sorted Inversions (Least to Most):")
for source_name, inversions in inversions_list:
    print(f"{source_name} has {inversions} inversions")
print()
min_inversions_source = min(inversions_list, key=lambda x: x[1])
print(f"The source with the least inversions is {min_inversions_source[0]} with {min_inversions_source[1]} inversions.")