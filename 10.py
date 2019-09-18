koekjes = input("Hoeveel koekjes wil je maken?")

suiker = 0.3125
boter = 0.020833333333333332
bloem = 0.057291666666666664

suikernodig = suiker * float(koekjes)
boternodig = boter * float(koekjes)
bloemnodig = bloem * float(koekjes)

print("Voor het maken van", koekjes, "koekjes, heb je dit nodig:")
print("Suiker:", suikernodig, "cups")
print("Boter:", boternodig, "cups")
print("Bloem:", bloemnodig, "cups")
