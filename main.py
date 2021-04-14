import requests  
import json   
from datetime import datetime as dt   

url = 'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow'  #API endpoint for getting all the questions on SO

response = requests.get(url)

def get_all():  #list all the questions on SO
	  

	for idx, question in enumerate(response.json()['items']):

		print('The title of Q{} is: {}'.format(idx+1, question['title']))
		print('The link to Q{} is: {}'.format(idx+1, question['link']))
		



def get_unaswered():  #list all the questions on the query date
	print('The list of unanswered questions on {} are: '.format(dt.now()))

	for idx, question in enumerate(response.json()['items']):
		if question['answer_count'] == 0:
			print('Q{} : {}'.format(idx+1, question['title']))
			print()



url = 'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow'

print(get_all())

print(get_unaswered())