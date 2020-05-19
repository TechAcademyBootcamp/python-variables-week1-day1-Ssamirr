# You can find these measures on the web (try wikipedia), but just in case:
# • 1 gallon is equivalent to 3.7854 liters
# • 1 barrel of oil produces 19.5 gallons of gas (approximately, can vary depending on the oil
# source. This number will work for us). FYI, a barrel is 42 gallons.
# • 1 gallon of gas produces approximately 20 pounds of CO2. Again, good enough
# • 1 gallon of gas produces 115,000 BTU (British Thermal Units). 1 gallon of ethanol
# produces 75,700 BTU.
# • God knows what the cost should be, but let’s peg it at $4.00/gallon
gallon=int(input("Gallon: "))
benzin= gallon*3.7854
barel=gallon*0.05
CO2=gallon*20
etanol=gallon*115000/75700
dollar=gallon*4

print("Benzin:",benzin)
print("Barel:",barel)
print("CO2:",CO2)
print("Etanol:",etanol)
print("Dollar:",dollar)
    