import requests  #requests enable a client to make requests to a web server
import json      #json is a text-based format used to store and transmit data objects consisting of key-value pairs or array data types


#print(response.json())  #return the response as json.

#print(response.json()['items']) #Inspect the items attribute which contains the list of questions


def get_all(url):
	response = requests.get(url)  #send arequst to an API endpoint to get all questions

	for idx, question in enumerate(response.json()['items']):

		print('The title of Q{} is: {}'.format(idx+1, question['title']))
		print('The link to Q{} is: {}'.format(idx+1, question['link']))
		




url = 'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow'

print(get_all(url))  #get all questions on stack overflow