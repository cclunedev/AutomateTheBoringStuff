def displayInventory(inventory):
  print("Inventory:")
  itemTotal = 0
  for item in inventory:
    itemTotal += inventory[item]
    print (str(inventory[item]) + " " + item)
  print('\nTotal number of items: ' + str(itemTotal))



def addToInventory(inventory, addedItems):
  for item in addedItems:
    if item in inventory:
      inventory[item] += 1
    else:
      inventory[item] = 1
  
  return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)




#playerInv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#displayInventory(playerInv)