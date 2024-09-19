# purwadhika-capstone1
# **README**
--
This app is created for my Purwadhika capstone project 1. This app is an order management system(OMS) that have capabilities to view, create, update and delete an order. 

This program was built using Python without any library being used.

The app is not connected to database so any changes will not be saved and will be back to it's default value everytime the program is rerun.

The data is stored in library within library format with the unique key is the order number.
Below is the keys and value within each order number
- Order ID - 
- Customer Name
- Item Name
- Payment Method → Credit card, Bank Transfer, e-Wallet 
- Invoice Status →  Paid, Expired, Waiting for Payment, Refund 
- Order status → Waiting for Payment, Processing, In Progress Delivery, Shipped, Cancelled

---

## **Intro to the App**
--
![alt text](image.png)

Above is the main menu for the order management system. The app have a few features that can be used by the user and the features are as listed below :
- View Order
- Create New Order
- Update an Order
- Delete an Order

---

## **View Order Menu**
![alt text](image-1.png)

Above is the main menu for view order. The view order menu have a few features that can be utilized by the user based on their needs. The features are as listed below :
- View All Order
- View Order by Invoice Status
- View Order by Order Status
- Search by Order ID

### **View All Order**
![alt text](image-2.png)

As shown above, if the user choose the option 1, the program will show all the data stored in the library.

### **View Order by Invoice Status**
![alt text](image-3.png)

As shown above, if the user choose the option 2 the program will ask the user to choose which invoice status that the user want to see. 

![alt text](image-4.png)

If the user input the number of invoice status options and the data with the designated invoice status is detected it will be shown as shown in the screenshot above.

### **View Order by Order Status**
![alt text](image-5.png)

As shown above, if the user choose the option 3 the program will ask the user to choose which order status that the user want to see. 

![alt text](image-6.png)

If the user input the number of order status options and the data with the designated order status is detected it will be shown as shown in the screenshot above.

### **View Order by Search Order ID**
![alt text](image-7.png)

As shown above, if the user choose the option 4 the program will ask the user to input the OrderID that they want to see. 

![alt text](image-8.png)

If the order that the user input is available in the library, then the program will show the order that the user search.

![alt text](image-9.png)

If not the program will return 'Order Not Found' and the user can proceed to enter new input again.

---

## **Create New Order Menu**
![alt text](image-10.png)

As shown above if the user choose the 2nd menu, it will ask the user to add new order number and the latest order number is also printed as a reminder for the user.

![alt text](image-11.png)

If the user input order number that already exist it will return error as shown above

![alt text](image-12.png)

If the user input order number that not exist yet it will ask the user to complete the add order process by entering necessary data as shown above and after all of it is done the next oreder will be added to the library.

---

## **Update Order Menu**
![alt text](image-13.png)

As shown above, the update menu consist of 2 main function which are :
- Update order invoice status
- Update order order status

### **Update Invoice Status**
![alt text](image-14.png)

If the user choose menu 1, the program will ask the user to input the order ID that they want to update, if the order is not found it will return message 'Order Not Found' and will go back to the update menu

![update invoice success](image-15.png)
If the order is found it will ask the user to input the updated status, after the user input the invoice status will be updated accordingly.

### **Update Order Statu**
![update order status success](image-16.png)

Same as updating invoice status, the program will ask to input the order ID and if found it will ask user to input the updated status. After the input the program will change the order status accordingly.

--- 

## **Delete Order**
![alt text](image-17.png)

When the user choose the delete order menu, the user will be asked to input the Order ID of the order that the user want to delete. If found the user will be asked to reconfirm whether they want to delete the order or not

if the user input 1, the order will be deleted as shown below
![success delete](image-19.png)

if the user input 2, cancel order program will be cancelled
![cancel delete](image-18.png)
