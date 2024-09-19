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
<img width="216" alt="image" src="https://github.com/user-attachments/assets/afafc43e-f28a-4ea3-8597-68ab4d740c73">


Above is the main menu for the order management system. The app have a few features that can be used by the user and the features are as listed below :
- View Order
- Create New Order
- Update an Order
- Delete an Order

---

## **View Order Menu**
<img width="289" alt="image-1" src="https://github.com/user-attachments/assets/654328b1-a2a5-4df0-a026-004fb1ced2ed">

Above is the main menu for view order. The view order menu have a few features that can be utilized by the user based on their needs. The features are as listed below :
- View All Order
- View Order by Invoice Status
- View Order by Order Status
- Search by Order ID

### **View All Order**
<img width="745" alt="image-2" src="https://github.com/user-attachments/assets/b54cf8c0-a595-44a2-a240-6336dd2dc81a">

As shown above, if the user choose the option 1, the program will show all the data stored in the library.

### **View Order by Invoice Status**
<img width="276" alt="image-3" src="https://github.com/user-attachments/assets/e125ee83-9136-48b0-8713-454466723ea8">

As shown above, if the user choose the option 2 the program will ask the user to choose which invoice status that the user want to see. 

<img width="704" alt="image-4" src="https://github.com/user-attachments/assets/f20f0644-90c5-4bb6-9f0c-edb46113bb0a">

If the user input the number of invoice status options and the data with the designated invoice status is detected it will be shown as shown in the screenshot above.

### **View Order by Order Status**
<img width="315" alt="image-5" src="https://github.com/user-attachments/assets/22911265-c4d0-44c4-9df4-3372abdb9cb8">

As shown above, if the user choose the option 3 the program will ask the user to choose which order status that the user want to see. 

<img width="670" alt="image-6" src="https://github.com/user-attachments/assets/0a589f4b-faaa-4d4b-a302-12fdf79d8973">

If the user input the number of order status options and the data with the designated order status is detected it will be shown as shown in the screenshot above.

### **View Order by Search Order ID**
<img width="295" alt="image-7" src="https://github.com/user-attachments/assets/3c16acb0-302c-4ac7-8ea3-91478f6b5806">

As shown above, if the user choose the option 4 the program will ask the user to input the OrderID that they want to see. 

<img width="679" alt="image-8" src="https://github.com/user-attachments/assets/c6cd80f9-0bc7-46c3-a0e2-cd7174833d3a">

If the order that the user input is available in the library, then the program will show the order that the user search.

<img width="208" alt="image-9" src="https://github.com/user-attachments/assets/1c72d36a-13e0-49ec-bbbb-1c549089c2f7">

If not the program will return 'Order Not Found' and the user can proceed to enter new input again.

---

## **Create New Order Menu**
<img width="284" alt="image-10" src="https://github.com/user-attachments/assets/01ccbea4-3a29-4a8f-b1fc-5fab437d1bff">

As shown above if the user choose the 2nd menu, it will ask the user to add new order number and the latest order number is also printed as a reminder for the user.

<img width="448" alt="image-11" src="https://github.com/user-attachments/assets/c7fe8e94-b753-48f2-bdc6-9fb89da6c512">

If the user input order number that already exist it will return error as shown above

<img width="334" alt="image-12" src="https://github.com/user-attachments/assets/7a6b29c7-1109-484d-9bd1-0674805588af">

If the user input order number that not exist yet it will ask the user to complete the add order process by entering necessary data as shown above and after all of it is done the next oreder will be added to the library.

---

## **Update Order Menu**
<img width="279" alt="image-13" src="https://github.com/user-attachments/assets/e53e3c63-67df-47ac-b7de-6b506f955527">

As shown above, the update menu consist of 2 main function which are :
- Update order invoice status
- Update order order status

### **Update Invoice Status**
<img width="238" alt="image-14" src="https://github.com/user-attachments/assets/891ded4e-a2a1-49ef-a56f-c9e5ff3ec413">

If the user choose menu 1, the program will ask the user to input the order ID that they want to update, if the order is not found it will return message 'Order Not Found' and will go back to the update menu

<img width="682" alt="image-15" src="https://github.com/user-attachments/assets/1fb3e6f0-7db0-4497-9ce1-e62022d1f18e">
If the order is found it will ask the user to input the updated status, after the user input the invoice status will be updated accordingly.

### **Update Order Statu**
<img width="667" alt="image-16" src="https://github.com/user-attachments/assets/41840fb1-16ec-49bf-9545-ef6aa96dac7b">

Same as updating invoice status, the program will ask to input the order ID and if found it will ask user to input the updated status. After the input the program will change the order status accordingly.

--- 

## **Delete Order**
<img width="552" alt="image-17" src="https://github.com/user-attachments/assets/956fa9a4-0400-43bd-8ed2-3f8a9a108e36">

When the user choose the delete order menu, the user will be asked to input the Order ID of the order that the user want to delete. If found the user will be asked to reconfirm whether they want to delete the order or not

if the user input 1, the order will be deleted as shown below
<img width="582" alt="image-19" src="https://github.com/user-attachments/assets/8a2d9151-d641-44f6-8884-7d133441d7b2">

if the user input 2, cancel order program will be cancelled
<img width="553" alt="image-18" src="https://github.com/user-attachments/assets/80ea0261-ec09-4c44-93e5-124aa2fb53a5">
