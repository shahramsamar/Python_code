import requests
import json
import pyttsx3

class coindesk():
    def __init__(self):
        self.engine = pyttsx3.init()
        
    def get_btc_price(self) :   
        res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = json.loads(res.text)
        # print(data['bpi']['USD']['rate'])
        btc_price = data['bpi']['USD']['rate']
        btc_price = int(float(btc_price.replace(',',"")))
        print("bitcoin price is {}".format(btc_price))
        self.engine.say("bitcoin price is {}".format(btc_price))
        self.engine.runAndWait()

btc = coindesk()
btc.get_btc_price()