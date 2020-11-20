# from tkinter import *
# import requests
# import json


# pycrypto = Tk()
# pycrypto.title("My crypto Portfolo")
# name = Label(pycrypto, text ="Bitcoin", bg ="black", fg ="white")
# name.grid(row=0, column=0, sticky=N+S+E+W)

# pycrypto.mainloop()

# print("programme completed")

# def my_portfolio:
#   api_requests = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=861d0cdf-b591-48af-8d91-524bf9aeaeb9")
#    api = json.loads(api_requests.content)


#  coins = [
#             {"symbol":"BTC",
#           "amount_owned":2,
#           "price_per_coin":3200
#             },
#             {
#             "symbol":"EOS",
#            "amount_owned":100,
#             "price_per_coin":2.05
#             }
#         ]
#  for i in range(0, 10):
#     for coin in coins:
#         if api["data"][i]["symbol"] ==coin["symbol"]:
#           total_paid = coin["amount_owned"] * coin["price_per_coin"]
#           profit = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
#           total_profit = profit * coin["price_per_coin"]
           
        

#           print (api["data"][i]["name"] +"---"+ api["data"][i]["symbol"]) 
#           print(total_paid)
#           print("total profit;","${0:.2f}".format(total_profit))
#           print("profit:","${0:.2f}".format(profit))
#           print("number of coin",coin["amount_owned"])
#           print("price = ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
#           print("----------------")



from tkinter import *
import requests
import json

from tkinter import *
pycrypto.title("My Pycrypto file")

def my_portfolio():
   api_requests = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=861d0cdf-b591-48af-8d91-524bf9aeaeb9")
   api = json.loads(api_requests.content)


   coins = [
            {"symbol":"BTC",
          "amount_owned":2,
          "price_per_coin":3200
            },
            {
            "symbol":"EOS",
           "amount_owned":100,
            "price_per_coin":2.05
            }
total pl=0            
    # coin_row = 1        
    for i in range(0, 10):
       for coin in coins:
            if api["data"][i]["symbol"] ==coin["symbol"]:
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
            pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
            total_profit = pl_percoin * coin["amount_owned"]

            total_pl = total + total_profit
           
        

            print (api["data"][i]["name"] +"---"+ api["data"][i]["symbol"]) 
            print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("total profit;","${0:.2f}".format(total_profit))
            print("Total amount paid:", "${0:.2f}".format(total_paid))
            print("current value:", "${0:.2f}".format(current_value))
            print("profit:","${0:.2f}".format(pl_percoin))
            print("number of coin",coin["amount_owned"])
            # print("price = ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("----------------")
print(total pl)            

            name = Label(pycrypto, text = "api["data"][i]["symbol"])", bg="grey", fg="black")
            name.grid(row=coin_row, column=0, sticky=N+W+S+E)

            price = Label(pycrypto, text = "total_paid", bg="white", fg="black")
            price.grid(row=coin_row, column=1, sticky=N+W+S+E)

            no_coin = Label(pycrypto, text = ""amount_owned", bg="grey", fg="black")
            no_coin.grid(row=coin_row, column=2, sticky=N+W+S+E)

            amount_paid = Label(pycrypto, text = "api["data"][i]["quote"]["USD"]["price"", bg="white", fg="black")
            amount_paid.grid(row=coin_row, column=3, sticky=N+W+S+E)

            profit= Label(pycrypto, text = "profit", bg="grey", fg="black")
            profit.grid(row=0, column=4, sticky=N+W+S+E)

            total_profit= Label(pycrypto, text = "total_profit", bg="white", fg="black")
            total_profit.grid(row=0, column=5, sticky=N+W+S+E)
             
            coin_row = coin_row +1 

name = Label(pycrypto, text = "Coin name", bg="#142E54", fg="black")
name.grid(row=0, column=0, sticky=N+W+S+E)

price = Label(pycrypto, text = "Price", bg="#142E54", fg="black")
price.grid(row=0, column=1, sticky=N+W+S+E)

no_coin = Label(pycrypto, text = "Coin owned", bg="#142E54", fg="black")
no_coin.grid(row=0, column=2, sticky=N+W+S+E)

amount_paid = Label(pycrypto, text = "Total Amount paid", bg="#142E54", fg="black")
amount_paid.grid(row=0, column=3, sticky=N+W+S+E)

profit= Label(pycrypto, text = "profit", bg="#142E54", fg="black")
profit.grid(row=0, column=4, sticky=N+W+S+E)

total_profit= Label(pycrypto, text = "total_profit", bg="#142E54", fg="black")
total_profit.grid(row=0, column=5, sticky=N+W+S+E)

my_portfolio()

pycrypto.mainloop()

print("test line")