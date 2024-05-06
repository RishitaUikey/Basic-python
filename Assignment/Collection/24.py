'''Write a  Python program to calculate the maximum aggregate from the list of tuples (pairs).
Sample Output:
Original list:
[('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]
Maximum aggregate value of the said list of tuple pair:
('Juan Whelan', 212)'''


original_list = [('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]

aggregate_scores = {}

for name, score in original_list:
    if name in aggregate_scores:
        aggregate_scores[name] += score
    else:
        aggregate_scores[name] = score

max_aggregate = max(aggregate_scores.items(), key=lambda x: x[1])


print("Maximum aggregate value of the said list of tuple pair:")
print(max_aggregate)
