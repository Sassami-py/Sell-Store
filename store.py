import random

gold= random.randint(100,500)
sword= random.randint(10,50)
shield= random.randint(10,50)
bag=[]
price=0
item=""

print("--Wellcome to store!--")
print(f"\nThe sword cost {sword}g and shield cost {shield}g!")

while gold>0:
  print(f"\nYou have {gold} golds")
  shop=input("\nChose if you want to buy a sword, a shield or if you want to exit: ").upper()
  if shop == "SWORD":
    price,item = sword,"Sword"
  elif shop == "SHIELD":
    price,item = shield,"Shield"
  elif shop == "EXIT":
    break
  else:
    print("\nInvalid option")
    continue

  if gold>=price:
    gold-=price
    bag.append(item)
    print(f"\nSuccess, you bag now have {bag}!")
  else:
    dif=price-gold
    print (f"\nYou don't have gold enough, you need {dif}g to buy this item!")
    continue
print(f"\nYou go out of the store with {bag} itens!")
print(f"\nYou have {gold}g left!")
