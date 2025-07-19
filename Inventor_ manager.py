inventory={"pen":10,
           "pencil":5,
           "cornflakes":1220}

while True:
    choice=input("Enter your choice: \n1. Add item\n2. Update price of an item \n3. Find item in a price range\n4.press anthing else to quit" \
)
    if choice=='1':
        item=input('Enter the item you want to add:')
        price=int(input('Enter the price of the item:'))
        inventory[item]=price
        print("Update inventory:",inventory)
        
    elif choice=='2':
        item=input('Enter the item you want to update:')
        if item in inventory:
                 price=int(input('Enter the new price of the item:'))
                 inventory[item]=price
                 print("Update inventory:",inventory)
                
        else:
                print("Item not found in inventory.Press 1 to add item")
    elif choice=='3':
          min_price=int(input('Enter the minimum price:'))
          max_price=int(input('Enter the maximum price:'))
          for item in inventory:
                price=inventory[item]
                if price>min_price and price<max_price:
                      print(f'{item }:{inventory[item]}, within the price range {min_price}-{max_price}')
          
    else:
          break