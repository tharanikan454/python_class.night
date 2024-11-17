#Shallow Copy
import copy
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)
original_list[0][0] = 10
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)

#Deep Copy
import copy
original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)
original_list[0][0] = 10
print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)

