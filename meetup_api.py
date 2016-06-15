#encoding=utf8
from __future__ import unicode_literals

import requests
import json
import time
import codecs
import sys
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)



def group_finder(cities):
	error_count = 0
       
       	api_key= ""
        

	#print "Hello"

       	for (city, state) in cities:
       		per_page = 200
      		results_we_got = per_page
      		offset = 0
	#	print "CITY STATE"
		params = {"sign":"true","country":"US", "state":state, "city":city, "radius": 10, "key":api_key, "page":per_page, "offset":offset }
       		while (results_we_got == per_page):
                	
			response=getResponse(**params)
	#		print "before sleep"
       			time.sleep(1)
	#		print "after sleep"
              		offset += 1
	#		print response

	#		print "after response"
              		results_we_got = response['meta']['count']
			
               		for group in response['results']:
	#			print "final loop"
				try:
	#				print "inside try"
					print ("," .join(map(unicode, [city, group['name'].replace(","," "), group['created'], group['city'],group.get('state',""),group['members'], group.get('who',"").replace(","," ")]))).encode("utf-8")
       					#time.sleep(1)
				except:
					error_count += 1
					
	print error_count


def getResponse(**params):
	request = requests.get("http://api.meetup.com/2/groups",params=params)
	data = request.json()
	return data



