subtotal = float(input("Enter the subtotal: "))
num_people = int(input("Enter the number of people: "))
tax_amount = subtotal * 0.085
tip_amount = subtotal * 0.20
print("Tip amount:", f"{tip_amount:.2f}")
print("Tax amount:", f"{tax_amount:.2f}")
print("Total amount:", f"{subtotal + tax_amount + tip_amount:.2f}")
print("Amount per person:", f"{(subtotal + tax_amount + tip_amount) / num_people:.2f}")
total_bill = subtotal + tax_amount + tip_amount
per_person = total_bill / num_people

#Value add

drink_subtotal = float(input("Enter the drink subtotal: "))
drink_tax_amount = drink_subtotal * 0.085
total_drink_amount = drink_subtotal + drink_tax_amount

print("Drink subtotal", f"{drink_subtotal:.2f}") 
print("Drink tax amount", f"{drink_tax_amount:.2f}")
print("Amount per person for second round of drinks:", f"{(total_drink_amount + drink_tax_amount) / num_people:.2f}")
print("Total amount per person including drinks:", f"{(total_bill + total_drink_amount)/ num_people:.2f}")

