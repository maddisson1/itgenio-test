def minimum(arr):
    min_row_index = 0
    min_col_index = 0
    min_row_sum = sum(arr[0])
    
    min_col_sum = 0
    for i in range(len(arr)):
        min_col_sum += arr[i][0]
        
    for i in range(1, len(arr)):
        row_sum = sum(arr[i])
        if row_sum < min_row_sum:
            min_row_sum = row_sum
            min_row_index = i
    
        
    for j in range(1, len(arr[0])):
        col_sum = 0
        for k in range(len(arr)):
            col_sum += arr[k][j]
        if col_sum < min_col_sum:
            min_col_sum = col_sum
            min_col_index = j
            
    return [min_row_index, min_col_index]
        
print(minimum([[7, 2, 7, 2, 8],
               [2, 9, 4, 1, 7],
               [3, 8, 6, 2, 4],
               [2, 5, 2, 9, 1],
               [6, 6, 5, 4, 5]]))

print(minimum([[-7, -2, -7, -2, -8],
               [-2, -9, -4, -1, -7],
               [-3, -8, -6, -2, -4],
               [-2, -5, -2, -9, -1],
               [-6, -6, -5, -4, -5]]))