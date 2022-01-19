# stream
#
# stream
#
# "p1 sell s1 1500 200"
# "p2 buy s2 900 500"
# "p3 buy s1 600 250"
# "p4 buy s1 1200 270",
# "p5 sell s3 300	800",
# "p6	sell s3 100	750",
# "p7 buy s3 500 900",
# "p20 sell s4 200 100",
# "p21 sell s4 200 150",
# "p22 buy  s4 200 300",
# "p33 buy  s4 100 350"
# "p10 sell s2 1000 400"

class Trade:

    buylist = []
    selllist = []
    def sell(data ):
    buylist.append(data)

def buy(data):
    selllist.append(data)
    selllist.sort(data.price)

def updateList(data):
    pass



def trade():
    stock = selllist.pop(input(3).stock)
    seller = selllist.pop(input(3).person)
    buyer = buylist.pop(input(3).person)
    sell_qty = selllist.pop(input(3).qty)
    buy_qty = buylist.pop(input(3).qty)
    sell_price = selllist.pop(input(3).price)
    buy_price = buylist.pop(input(3).price)
    print(seller, ':', stock, ':', sell_qty, ':', sell_price)


input = ("p1 sell s1 1500 200")

     if input(2) == 'sell':
         sell(input)
     else :
         buy(input)

     if  input(2) =='buy' and input(3) in selllist:
        trade(input)
        updateList(input)





