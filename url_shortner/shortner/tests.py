# This is a test file. Update the data dictionary with
# the longurl that you want to make short.
# Run the application using 'python manage.py runserver'
# Update the IP & port in the post request.
# Then execute tests.py as a python script.
# You will see the result, status code & description of 
# the status code.

import requests

data = {'url':'www.nishantpassari.com'}

# Concatenating 'http://' if url doesn't starts with 'www.'
if 'www.' in data['url'][:4]:
    data['url'] = "http://" + data['url']

# Making post request
r = requests.post('http://127.0.0.1:8000/shortner/', data = data)

# Printing the results
print("After conversion->", r.text)
print("Status code is->", r.status_code)
print("Description of status code->", r.reason)