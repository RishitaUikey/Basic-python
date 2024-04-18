'''Write a  Python program to calculate the average value of the numbers in a given tuple of tuples.
Original Tuple:
((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Average value of the numbers of the said tuple of tuples:
[30.5, 34.25, 27.0, 23.25]
Original Tuple:
((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
Average value of the numbers of the said tuple of tuples:
[25.5, -18.0, 3.75]'''

def calculate_average(tuple_of_tuples):
    transposed = list(zip(*tuple_of_tuples))
    
    column_sums = [sum(column) for column in transposed]
    
    num_tuples = len(tuple_of_tuples)
    
    averages = [sum / num_tuples for sum in column_sums]
    
    return averages

tuples_of_tuples = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)), \
                   ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

for t in tuples_of_tuples:
    averages = calculate_average(t)
    print("Average value of the numbers of the said tuple of tuples:", averages)
