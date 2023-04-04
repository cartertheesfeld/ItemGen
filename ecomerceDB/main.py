import SQLServer as sql
import ItemGen as ig

server =  "localhost\SQLExpress"
database = "Carter's Business"

db = sql.SQLServer(server, database)

db.connect()

# Create item data
itemData = ig.CreateItemData()

# Print out the item data
print(itemData)

