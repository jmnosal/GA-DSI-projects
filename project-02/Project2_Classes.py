class OSM:
    #Creates a new Online Store Machine that creates new stores of a given inventory type
    def __init__(self, name, *args):
        self.number_of_stores = 0
        self.list_of_stores = []
        self.type_of_inv = list(args)
        self.name = name

    def createOnlineStore(self, store):
        # create new instance of Class OnlineStore
        self.list_of_stores.append(store)
        self.number_of_stores += 1
        return OnlineStore(store, [x for x in self.type_of_inv]) #The function passes the store name and the inventory types
        # to the OnlineStore instance

class OnlineStore:
    #Online stores that receive and sell inventory of a type inherited from the OSM
    def __init__(self, name, *args):
        self.name = name
        self.type_of_inv = list(args)[0]
        self.inventory = {k:0 for k in self.type_of_inv}
        self.inventorySold = {k:0 for k in self.type_of_inv}
        self.customerList = []

    def addInventory(self, type_of_inventory, amount):
        # add inventory to 'inventory'
        if type_of_inventory not in self.inventory:
            print 'This type of inventory not sold here.' #Check to ensure the type of inventory is sold at the store
        else:
            self.inventory[type_of_inventory] += amount
        return self.inventory


    def sellInventory(self, type_of_inventory, amount):
        #remove inventory from 'inventory' and assign to customer purchase history
        if type_of_inventory not in self.inventory:
            print 'This type of inventory not sold here.' #Check to ensure the type of inventory is sold at the store
        else:
            self.inventory[type_of_inventory] -= amount
            self.inventorySold[type_of_inventory] += amount
        return self.inventory


    def summaryInventory(self):
        # summarize current inventory levels
        print '{0} has a current inventory of: {1}'.format(self.name, self.inventory)
        return self.inventory


    def addCustomer(self, name):
        # creates a new instance of class Customer and assigns it to the OnlineStore customerList
        self.customerList.append(name)
        return Customer(name, self.name, [x for x in self.type_of_inv])


    def summarizePurchaseHistory(self):
        # totals all purchases minus returns for all customers
        print '{0} has sold the following items: {1}'.format(self.name, self.inventorySold)
        return self.inventorySold


    def storeProfile(self):
        #summary of a store's inventory type, number of customers and who they are
        print '{0} is a store that sells {1}. It currently has {2} customers, who are: {3}'.format\
              (self.name, self.type_of_inv, len(self.customerList), self.customerList)

class Customer:
    #Customers have unique names and can purchase items from the stores that create them
    def __init__(self, name, inst, *args):
        self.purchaseHistory = {}
        self.name = name
        self.type_of_inv = list(args)[0]
        self.inst = inst

    def purchaseItem(self, item, quantity, store):
        #Purchase items from the OnlineStore
        if item not in self.type_of_inv:
            print 'That type of product not sold in this store.' #Checks if the item requested is sold at the store
        else:
            if store.inventory[item] - quantity < 0:
                print "{0} does not have enough {1} to place the order.".format(self.inst, item) #Checks that the item is in stock
            elif item not in self.purchaseHistory.keys():
                self.purchaseHistory[item] = quantity
                store.sellInventory(item, quantity) #Adds a new Key/value pair to the customer's purchase dictionary if it is a new item
            else:
                self.purchaseHistory[item] = self.purchaseHistory[item] + quantity
                store.sellInventory(item, quantity) #Adds the quantity

        return {item:quantity}
        #assigns an item to the customer purchaseHistory and subtracts it from the store inventory

    def customerProfile(self):
        print 'This is {0}, who is a customer of {1} and has purchased the following items: {2}'.format(self.name, self.inst, self.purchaseHistory)

Books = OSM('Books', 'books', 'cds', 'newspaper')
Borders = Books.createOnlineStore('Borders')
print Borders.inventory
Borders.addInventory('cds', 100)
Borders.addInventory('books', 200)
Borders.addInventory('fish', 50)
print Borders.inventory
print Borders.inventorySold
Borders.storeProfile()
Bob = Borders.addCustomer('Bob')
Borders.storeProfile()
Bob.customerProfile()
Bob.purchaseItem('cds', 50, Borders)
Borders.summarizePurchaseHistory()
Bob.customerProfile()
Bob.purchaseItem('newspaper', 2, Borders)

