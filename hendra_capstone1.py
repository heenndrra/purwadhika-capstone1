listOrder = {
    'order1' : {'OrderID':'1', 'Nama': 'Hendra', 'Item': 'Keyboard', 'Payment Method':'Credit Card', 'Invoice Status':'Paid', 'Order Status': 'Processing'},
    'order2' : {'OrderID':'2', 'Nama': 'Clara', 'Item': 'Mouse', 'Payment Method':'Bank Transfer', 'Invoice Status':'Waiting for Payment', 'Order Status': 'Waiting for Payment'},
    'order3' : {'OrderID':'3', 'Nama': 'Hendy', 'Item': 'Monitor', 'Payment Method':'Bank Transfer', 'Invoice Status':'Paid', 'Order Status': 'Shipped'},
    'order4' : {'OrderID':'4', 'Nama': 'Devin', 'Item': 'Mouse', 'Payment Method':'e-wallet', 'Invoice Status':'Paid', 'Order Status': 'Shipped'}
}
lastOrder = list(listOrder.keys())[-1]

def viewOrder():
    while True: 
        pilihMenu = int(input('=== View Order Menu === \n1. View All Order \n2. View Order by Invoice Status \n3. View Order by Order Status \n4. Search by Order ID \n0. Back to Main Menu \nChoose Your Option  :'))
        if pilihMenu == 1 :
            print('=== View All Order === ')
            print('OrderID\t|Nama\t|Item\t|Payment Method\t|Invoice Stauts\t\t|Order Status')
            for key in listOrder.keys():
                print("{}\t|{}\t|{}\t|{}\t|{}\t|{}\t".format(listOrder[key]['OrderID'],listOrder[key]['Nama'],listOrder[key]['Item'],listOrder[key]['Payment Method'],listOrder[key]['Invoice Status'],listOrder[key]['Order Status'])) 
                continue
        elif pilihMenu == 2:
            while True: 
                invoiceStatus = int(input('=== Invoice Status View === \n1. Waiting for Paymet \n2. Expired \n3. Paid \n0. Back to View Order Menu \nChoose Your Option : '))
                if invoiceStatus == 1 :
                    print('OrderID\t|Nama\t|Item\t|Payment Method\t|Invoice Stauts\t\t|Order Status')
                    for key in listOrder.keys():
                        if listOrder[key]['Invoice Status'] == 'Waiting for Payment' :
                            print("{}\t|{}\t|{}\t|{}\t|{}\t|{}\t".format(listOrder[key]['OrderID'],listOrder[key]['Nama'],listOrder[key]['Item'],listOrder[key]['Payment Method'],listOrder[key]['Invoice Status'],listOrder[key]['Order Status']))
                        else :
                            continue
                elif invoiceStatus == 2 :
                    print('OrderID\t|Nama\t|Item\t|Payment Method\t|Invoice Stauts\t\t|Order Status')
                    for key in listOrder.keys():
                        if listOrder[key]['Invoice Status'] == 'Expired' :
                            print("{}\t|{}\t|{}\t|{}\t|{}\t|{}\t".format(listOrder[key]['OrderID'],listOrder[key]['Nama'],listOrder[key]['Item'],listOrder[key]['Payment Method'],listOrder[key]['Invoice Status'],listOrder[key]['Order Status']))
                        else :
                            continue
                elif invoiceStatus == 3 :
                    print('OrderID\t|Nama\t|Item\t|Payment Method\t|Invoice Stauts\t\t|Order Status')
                    for key in listOrder.keys():
                        if listOrder[key]['Invoice Status'] == 'Paid' :
                            print("{}\t|{}\t|{}\t|{}\t|{}\t|{}\t".format(listOrder[key]['OrderID'],listOrder[key]['Nama'],listOrder[key]['Item'],listOrder[key]['Payment Method'],listOrder[key]['Invoice Status'],listOrder[key]['Order Status']))
                        else :
                            continue
                elif invoiceStatus == 0 :
                    break
                else : 
                    print("Option's not Found")
        elif pilihMenu == 3:
            while True: 
                orderStatus = int(input('=== Order Status View === \n1. Waiting for Payment \n2. Processing \n3. In Progress Delivery \n4. Shipped \n0. Back to View Order Menu \nChoose Your Option : '))
                if orderStatus == 1 :
                    print('OrderID\t|Nama\t|Item\t|Payment Method\t|Invoice Stauts\t\t|Order Status')
                    for key in listOrder.keys():
                        if listOrder[key]['Order Status'] == 'Waiting for Payment' :
                            print("{}\t|{}\t|{}\t|{}\t|{}\t|{}\t".format(listOrder[key]['OrderID'],listOrder[key]['Nama'],listOrder[key]['Item'],listOrder[key]['Payment Method'],listOrder[key]['Invoice Status'],listOrder[key]['Order Status']))
                        else :
                            continue
                elif orderStatus == 2 :
                    print('OrderID\t|Nama\t|Item\t|Payment Method\t|Invoice Stauts\t\t|Order Status')
                    for key in listOrder.keys():
                        if listOrder[key]['Order Status'] == 'Processing' :
                            print("{}\t|{}\t|{}\t|{}\t|{}\t|{}\t".format(listOrder[key]['OrderID'],listOrder[key]['Nama'],listOrder[key]['Item'],listOrder[key]['Payment Method'],listOrder[key]['Invoice Status'],listOrder[key]['Order Status']))
                        else :
                            continue
                elif orderStatus == 3 :
                    print('OrderID\t|Nama\t|Item\t|Payment Method\t|Invoice Stauts\t\t|Order Status')
                    for key in listOrder.keys():
                        if listOrder[key]['Order Status'] == 'In Progress Delivery' :
                            print("{}\t|{}\t|{}\t|{}\t|{}\t|{}\t".format(listOrder[key]['OrderID'],listOrder[key]['Nama'],listOrder[key]['Item'],listOrder[key]['Payment Method'],listOrder[key]['Invoice Status'],listOrder[key]['Order Status']))
                        else :
                            continue
                elif orderStatus == 4 :
                    print('OrderID\t|Nama\t|Item\t|Payment Method\t|Invoice Stauts\t\t|Order Status')
                    for key in listOrder.keys():
                        if listOrder[key]['Order Status'] == 'Shipped' :
                            print("{}\t|{}\t|{}\t|{}\t|{}\t|{}\t".format(listOrder[key]['OrderID'],listOrder[key]['Nama'],listOrder[key]['Item'],listOrder[key]['Payment Method'],listOrder[key]['Invoice Status'],listOrder[key]['Order Status']))
                        else :
                            continue
                elif orderStatus == 0 :
                    break
                else : 
                    print("Option's not Found")
        elif pilihMenu == 4:
            while True:
                searchOrder()
                break
        elif pilihMenu == 0:
            break
        else :
            print("Option's not Found")

def addPayment():
    addPayment = ''
    while True:
        addPayment = int(input('=== Payment Options === : \n1. Bank Transfer \n2. Credit Card \n3. e-Wallet \nChoose Payment Method : '))
        if addPayment == 1 :
            addPayment = 'Bank Transfer'
            break
        elif addPayment == 2 :
            addPayment = 'Credit Card'
            break
        elif addPayment == 3:
            addPayment = 'e-Wallet'
            break
        else :
            print('Option Entered Not Found, Please Choose Only Available Options')        
    return addPayment

def createOrder():
    while True:
        print(f'Last Order Number is {lastOrder}')
        inputOrder = input('Masukan Order Number :')
        finalInput = inputOrder.replace(' ','')
        if finalInput.lower() not in listOrder.keys():
            print("Please Add The Order Details")
            addID = input('Input Order ID : ')
            addName = input('Input Customer Name : ')
            addItem = input('Input Item Purchased : ')
            paymentMethod = addPayment()
            newStatus = 'Waiting for Payment'
            newOStatus= 'Waiting for Payment'
            listOrder[finalInput.lower()] = {'OrderID' : addID, 'Nama' : addName, 'Item' : addItem, 'Payment Method' :  paymentMethod, 'Invoice Status' : newStatus, 'Order Status': newOStatus}
            print('Order Successfully Added')
            break
        else :
            print('Order Number Already Exist, Please Input New One')
            
def searchOrder():
    orderFound = ''
    while True:
        inputOID = input('Masukan OrderID : ')
        for key in listOrder.keys():
            if inputOID in listOrder[key]["OrderID"]:
                orderFound = key
        if orderFound != '' :
            print('OrderID\t|Nama\t|Item\t|Payment Method\t|Invoice Stauts\t\t|Order Status')
            print("{}\t|{}\t|{}\t|{}\t|{}\t|{}\t".format(listOrder[orderFound]['OrderID'],listOrder[orderFound]['Nama'],listOrder[orderFound]['Item'],listOrder[orderFound]['Payment Method'],listOrder[orderFound]['Invoice Status'],listOrder[orderFound]['Order Status']))
            break
        else :
            print("Order Not Found")
            break
    return orderFound
        
def updateInvoice():
    while True:
        idToUpdate = searchOrder()
        if idToUpdate == '':
            break
        else :
            global order
            order = listOrder[idToUpdate]
            updateInvoice = int(input(f'=== Update Invoice === \n1. Paid\n2. Expired\n3. Refund\n0. Back to Update Menu\nChoose New Invoice Status For Order ID {order['OrderID']} : '))
            if updateInvoice == 1:
                order['Invoice Status'] = 'Paid'
                printResultUpdate()
                break
            elif updateInvoice == 2:
                order['Invoice Status'] = 'Expired'
                printResultUpdate()
                break
            elif updateInvoice == 3:
                order['Invoice Status'] = 'Refund'
                printResultUpdate()
                break
            elif updateInvoice == 0:
                break
            else:
                print('Please Input The Right Status')
   
def updateOrder():
    while True:
        idToUpdate = searchOrder()
        if idToUpdate == '':
            break
        else :
            global order
            order = listOrder[idToUpdate]
            updateOrder = int(input(f'=== Update Order === \n1. Processing\n2. In Progress Delivery\n3. Shipped\n4. Cancelled\n0. Back to Update Menu\nChoose New Order Status For Order ID {order['OrderID']} : '))
            if updateOrder == 1:
                order['Order Status'] = 'Processing'
                printResultUpdate()
                break
            elif updateOrder == 2:
                order['Order Status'] = 'In Progress Delivery'
                printResultUpdate()
                break
            elif updateOrder == 3:
                order['Order Status'] = 'Shipped'
                printResultUpdate()
                break
            elif updateOrder == 4:
                order['Order Status'] = 'Cancelled'
                printResultUpdate()
                break
            elif updateOrder == 0:
                break
            else:
                print('Please Input The Right Status')
   
def printResultUpdate():

    print('Update Successful!')
    print('OrderID\t|Nama\t|Item\t|Payment Method\t|Invoice Stauts\t\t|Order Status')
    print("{}\t|{}\t|{}\t|{}\t|{}\t|{}\t".format(order['OrderID'],order['Nama'],order['Item'],order['Payment Method'],order['Invoice Status'],order['Order Status']))

def updateFunction():
    while True:
        updateChoice = int(input('=== Update Menu ===\n1. Update Invoice Status\n2. Update Order Status\n0. Back to Main Menu\nChoose Update Options :'))
        if updateChoice == 1 :
            updateInvoice()
        elif updateChoice == 2:
            updateOrder() 
        elif updateChoice == 0:
            break
        else :
            print('Menu not Found')
        
def deleteFunction():
    while True:
        idToUpdate = searchOrder()
        order = listOrder[idToUpdate]
        deleteOrder = int(input(f'=== Delete Order Menu === \n1. Delete\n2. Cancel\nAre you sure you want to delete Order ID {order['OrderID']} : '))
        if deleteOrder == 1:
            listOrder.pop(idToUpdate)
            print('Order Successfully Deleted')
            break
        elif deleteOrder == 2:
            print('Delete Order Cancelled')
            break
        else:
            print('Please Input The Right Choice')


while True:
    pilihMenu = int(input('=== Main Menu === \n1. View Order \n2. Create New Order \n3. Update an Order \n4. Delete an Order \n0. Exit Program \nChoose Your Menu :'))
    if pilihMenu == 1:
        viewOrder() 
    elif pilihMenu == 2 :
        createOrder()
    elif pilihMenu == 3:
        updateFunction()
    elif pilihMenu == 4:
        deleteFunction()
    elif pilihMenu == 0:
        break
    else : 
        print('Menu not Found')

