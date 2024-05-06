'''Write a  Python class to get all possible unique subsets from a set of distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]'''


class SubsetGenerator:
    def __init__(self):
        pass

    def generate_subsets(self, nums):
        subsets = [[]]
        for num in nums:
            subsets += [curr_subset + [num] for curr_subset in subsets]
        return subsets

generator = SubsetGenerator()
input_nums = [4, 5, 6]
print("Input:", input_nums)
print("Output:", generator.generate_subsets(input_nums))
