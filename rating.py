import time
import urllib.request
import sys 
from pprint import pprint
import json

url = "https://koinex.in/api/ticker"

def data_parser(coin,what):
    req = urllib.request.Request(url)
    r=urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    pprint(cont['stats'][coin][what])

def main():
	par_1 = sys.argv[1]
	par_2 = sys.argv[2]
	while (True):
		time.sleep(5)
		data_parser(par_1,par_2)

if __name__ == '__main__':
	main()

