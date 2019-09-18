item1 = float(input("Wat is de prijs van product 1?"))
item2 = float(input("Wat is de prijs van product 2?"))
item3 = float(input("Wat is de prijs van product 3?"))
item4 = float(input("Wat is de prijs van product 4?"))
item5 = float(input("Wat is de prijs van product 5?"))

opgeteld = (item1 + item2 + item3 + item4 + item5)
tax = (opgeteld*0.07)
totaleprijs = (opgeteld + tax)

print("Alle producten bij elkaar kosten: ", opgeteld)
print("De tax is: ", tax)
print("De totale prijs is: ", totaleprijs)
