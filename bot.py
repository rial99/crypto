import time
import sys
import urllib.request
from pprint import pprint
import json

url = "https://koinex.in/api/ticker"

def data_parser(currency,coin):
    req = urllib.request.Request(url)
    r=urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    kota = float(cont['stats'][currency][coin]['lowest_ask'])
    pprint(cont['stats'][currency][coin]['lowest_ask'])
    return kota

def main():
	period = 10
	par_1 = 'inr'#sys.argv[1]
	par_2 = 'TRX'#sys.argv[2]
	while True:
		print("----")
		price_1=data_parser(par_1,par_2)
		time.sleep(period)
		price_2=data_parser(par_1,par_2)
		diff = price_2-price_1
		dydx = diff/period
		print("*dy/dx*: "+str(dydx))

if __name__ == "__main__":
	main()