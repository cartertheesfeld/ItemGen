import SQLServer as sql
import ItemGen as ig

server =  "localhost\SQLExpress"
database = "Carter's Business"

db = sql.SQLServer(server, database)

db.connect()

itemGenerator = ig.ItemGen()

# Create item data
itemData = itemGenerator.CreateItemData()

# Print out the item data
print(itemData)
for x in range(10000):
    itemData = itemGenerator.CreateItemData()
    db.send_data('items', itemData, columns=["itemName", "decription", "price"])
