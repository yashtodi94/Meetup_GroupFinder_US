
from __future__ import unicode_literals
from meetup_api import group_finder
import requests
import json
import time
import codecs
import sys
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)
cities = list()
params = dict()


def main():

       	#cities =[("Bridgeport","CT"),("New Haven","CT"),("Hartford","CT"),("Stamford","CT"),("Waterbury","CT")]
        api_key= ""
        
        per_page = 4
        res = per_page
        offset = 0
        params = {"sign":"true","country":"US", "key":api_key, "page":per_page }
        response=getResponse(**params)
        time.sleep(1)
        offset += 1
        res = response['meta']['count']
	for x in range(len(response["results"])):
		city = 	response["results"][x]["city"]
		state = response["results"][x]["state"]
		#print city, state
		tup = (city, state)
		cities.append(tup)
	print cities
	group_finder(cities)
		
		 
        	#time.sleep(1)


def getResponse(**params):

	request = requests.get("http://api.meetup.com/2/cities",params=params)
   	data = request.json()
	
	return data


if __name__=="__main__":
        main()


