# set จะไม่นับตัวที่ซ้ำ และไม่เรียงลำดับ
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# in operation
print('orange' in basket)
print('coconut' in basket)

# method
basket.add('grap')
basket.remove('orange')
basket.clear()
print(basket)

# set operation
basket1 = {'apple', 'orange', 'banana', 'coconut'}
basket2 = {'pear', 'banana', 'apple'}

# basket2.update(basket1)
# print(basket1)
# print(basket2)

# union
print(basket1.union(basket2))
print(basket1 | basket2)

# intersection
print(basket1 & basket2)
print(basket1.intersection(basket2))

# difference
print(basket1 - basket2)
print(basket1.difference(basket2))
