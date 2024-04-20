'''Write a Python program to extract specified number of elements from a given list, which follows each other continuously.
Original list:
[1, 1, 3, 4, 4, 5, 6, 7]
Extract 2 number of elements from the said list which follows each other continuously:
[1, 4]
Original lists:
[0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
Extract 4 number of elements from the said list which follows each other continuously:
[4]'''

def extract_continuous_elements(lst, num_elements):
    extracted_elements = []
    for i in range(len(lst) - num_elements + 1):
        if len(set(lst[i:i+num_elements])) == 1:
            extracted_elements.extend(lst[i:i+num_elements])
    return extracted_elements

original_list1 = [1, 1, 3, 4, 4, 5, 6, 7]
num_elements1 = 2
original_list2 = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
num_elements2 = 4
extracted_elements1 = extract_continuous_elements(original_list1, num_elements1)
extracted_elements2 = extract_continuous_elements(original_list2, num_elements2)
print("Original list:")
print(original_list1)
print(f"Extract {num_elements1} number of elements from the said list which follows each other continuously:")
print(extracted_elements1)

print("\nOriginal list:")
print(original_list2)
print(f"Extract {num_elements2} number of elements from the said list which follows each other continuously:")
print(extracted_elements2)
