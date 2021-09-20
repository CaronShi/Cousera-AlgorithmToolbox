#input = 3 50 60 20 100 50 120 30
#output = 180
n = 3
t_weight = 50
value_weight = 60,20,100,50,120,30
value = [i for i in value_weight[0::2]]
weight = [i for i in value_weight[1::2]]
unit_price_list = []
unit_price = []
sort_unit = []
for i in range(n):
    unit_price_list.append([value[i],weight[i]])
    unit_price.append(value[i]/weight[i])
sort_unit = sorted(unit_price,reverse = True)

#create a list match unit_price_list,unit_price

currentweight = t_weight
currentvalue = 0

for num in sort_unit: #16
    if weight[unit_price.index(num)] > t_weight:
        currentvalue = currentweight * num
        break
    else:
        if currentweight >0:
            currentweight -= weight[unit_price.index(num)]
            currentvalue += value[unit_price.index(num)]
        if currentweight <= 0:
            break
print(currentvalue)
