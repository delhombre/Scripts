#!/usr/bin/python3

without_vat = input("Enter price without vat : ")
without_vat = float(without_vat)

#### Compute vat and total price
vat_rate = 21.0
vat = (without_vat / 100) * vat_rate
total = without_vat + vat

#### Show total price
print("Your order total : " + str(total) + "€ vat included")
