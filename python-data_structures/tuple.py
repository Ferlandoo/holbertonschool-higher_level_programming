test_tup1 = (10, )
test_tup2 = (2, 5)

min_length = min(len(tuple1), len(tuple2))

# Sum the corresponding elements of the two tuples
sum_tuple = tuple(tuple1[i] + tuple2[i] if i < min_length else tuple1[i] if i < len(tuple1) else tuple2[i] for i in range(max(len(tuple1), len(tuple2))))

print("Sum of the tuples:", sum_tuple)


# printing result
print("Resultant tuple after addition : " + str(res))
