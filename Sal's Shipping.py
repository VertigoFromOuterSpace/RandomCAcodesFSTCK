weigth = 1.5
flatCharge = 20

# Ground Shipping
if weigth <= 2:
  print("Price:" , 1.50 * weigth + flatCharge)
elif weigth > 2 and weigth <= 6:
  print("Price:" , 3.00 * weigth + flatCharge)
elif weigth > 6 and weigth <= 10:
  print("Price:" , 4.00 * weigth + flatCharge)
elif weigth > 10:
  print("Price:" , 4.75 * weigth + flatCharge)

# Ground Shipping Premium
groundShippingPrice = 125.00
print("Price for Ground Shippping:", groundShippingPrice)

# Drone Shipping
if weigth <= 2:
  print("Price:" , 4.50 * weigth)
elif weigth > 2 and weigth <= 6:
  print("Price:" , 9.00 * weigth)
elif weigth > 6 and weigth <= 10:
  print("Price:" , 12.00 * weigth)
elif weigth > 10:
  print("Price:" , 14.25 * weigth)
