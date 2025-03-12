def two_sum(nums, target):
    # Dictionary to store number and its index
    index_map = {}
    
    # Loop through each number in the list
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # If the complement is in the map, return the indices
        if complement in index_map:
            return [index_map[complement], i]
        
        # Otherwise, store the index of the current number
        index_map[num] = i
        print(index_map)
nums = [2, 6,1, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
