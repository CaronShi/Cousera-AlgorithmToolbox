
# inputs
n = int (input ())
total_weight = int (input ())

# items = [(60, 20), (100, 50), (120, 30)]
items = [] 
for i in range (0, n):
    value = int (input ())
    weight = int (input ())
    item = (value, weight)
    items.append (item)

# sort items by ratio = value / weight
# where an item is a tuple of (value, weight)
sorted_items = sorted (items, key=lambda item: item [0]/item [1], reverse=True)

# fractional knapsack problem (greedy)
current_weight = 0
current_value = 0
for item in sorted_items:
    value, weight = item
    # if I have enough space
    if current_weight + weight <= total_weight:
        current_value += value
        current_weight += weight
    else: # if I don't have enough space
        # if I have space
        if current_weight < total_weight:
            remain_weight = total_weight - current_weight
            ratio = value / weight
            current_value += ratio * remain_weight
            current_weight += remain_weight
            break
        else: # if I don't have space (current_weight == total_weight)
            break

# outputs
print (current_value)


# execution 
# echo -e "3\n50\n60\n20\n100\n50\n120\n30\n" | python3 test.py

#python3 test.py << EOF # end of file
#> 3
#> 50
#> 60
#> 20
#> 100
#> 50
#> 120
#> 30
#> EOF
     

