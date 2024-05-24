class Orders:
    bill=0
    def __init__(self,item,price,desc,orders,code):
        self.item=item
        self.price=price
        self.desc=desc
        self.orders=orders
        self.code=code
    def pm(self):
        print(f'code: {self.code} \n{self.item}  Rs.{self.price}   Description: {self.desc}\n')
    

    
menu=[Orders('Pizza',200,'Italian',0,1),Orders('Burger',100,'American',0,2),Orders('Dosa',80,'Indian',0,3)]
def reset():
    for i in menu:
        i.orders=0
    Orders.bill=0
    global otn
    del(otn[:])
    print('Reset Successful!')
def pmenu():
    for j in menu:
        j.pm()
    print('Enter code 0 to reset')

def po():
    print('Orders till now:')
    for i in otn:
        print(f'{menu[i].item} x {menu[i].orders}')
    print(f'Total bill: Rs.{Orders.bill}')

otn=[]

try:

    while (True):
        pmenu()
        x= int(input('Enter food code: '))
        if x==0:
            reset()
            continue
        if x<0 or x>len(menu):
            print('Invalid Food code!')
            continue
        n= int(input('Enter quantity in numbers: '))
        menu[x-1].orders+=n
        Orders.bill+=menu[x-1].price*n
        otn.append(x-1)
        po()
        yn=input('Continue ordering? (y/n): ')
        if yn=='n':
            print('Thankyou for ordering!')
            break


except:
    print('Something went wrong. You might have entered Invalid input.')

    
