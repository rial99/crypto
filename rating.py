import urllib.request
import sys 
from pprint import pprint
import json
url = "https://koinex.in/api/ticker"

def data_parser(coin):
    req = urllib.request.Request(url)
    r=urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    pprint(cont['prices'][coin])

def main():
	par_1 = sys.argv[1]
	data_parser(par_1)

if __name__ == '__main__':
	main()

