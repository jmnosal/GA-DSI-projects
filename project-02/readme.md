
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2: Online Store Manager
#### Due Wednesday, November 16, 9 am

### Overview

Imagine that you own a website that allows your customers to create new Online Stores. An example of a webpage that offers that type of service is weebly.com. Take a moment to check out the site.

Your project for the 2nd week will be to create an OnlineStoreManager (OSM) as described below. Write out the story and create a diagram. Create a use case of your OSM and document your code appropriately. All transactions such as adding inventory and selling items have to go through the OnlineStore object.

Each object of the class OSM has a special method called CreateOnlineStore which creates an OnlineStore using a specific template specified by a list of Products that the store can sell. An example would be a store that offers Books, CDs, and News Papers. The specific OSM object can only create new stores that can sell the items specified in the template. The OSM object stores the number of stores it created and also stores a list of all of the stores it created.

Each newly created online store using the OSM template has a Name, an Inventory and a list of Customers. The inventory can hold only items defined in the template and are separated by item type. For example if the online store sells books then Inventory can hold items of type book. You can only add items to the inventory which the store can hold. You cannot sell items that you do not have. The online store has a method which allows you to summarize the inventory.

You can add customers to each online store. Each customer of an online store has a history of purchased items. The online store provides a method which allows you to summarize the purchase history of each of the store's customers.

You might find it useful to override the following methods: _repr_, _eq_, _add_. If you were to overload _eq_ for a hypothetical class Point for example you can use expressions such as:

```
if point in ListOfPoints
ListOfPoints.remove(point)
```

**Bonus and highly worth it:**
If you decide to overload the functions _getitem_ and _setitem_ you can access your objects using the [] - Operator. What other Operators can you overload in Python?


**Deliverables**: a Jupyter notebook, or .py file, with your well-commented code, and the story digram uploaded to github.  In your code, you should also include an implementation of the code.  Also write a blog entry of 300+ words describing your approach and design.
