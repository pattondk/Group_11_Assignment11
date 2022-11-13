'''
Name: David Patton and Josh Earley
email: pattondk@mail.uc.edu and earleyja@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Created a module that calls and API and creates a url
Citations: 
Anything else that's relevant: This was a group project 
'''
import json
import requests
response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?query=apple&pageSize=2&api_key=XN9jws7B0PKQGDqBWuhde8MqvJgV2Y8xo8Oj8XKp')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
  
print(parsed_json) 
print(parsed_json['totalHits'])

    
#for park in parsed_json['data']:
    #print (park)