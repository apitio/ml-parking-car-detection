import requests
import json

# The POST request's multipart_data dictionary. 
# This dict contains every necessary information for the requests module
# to assemble the required POST request.
multipart_data = {
	# This contains the image pointer. It can be a binary data too
    'image': ('test.jpg', open('test.jpg', 'rb')),
    # The other parameters. Notice that the first element of the tuple is None, 
	# because multipart/form-data is originally provided for file transfer, 
	# but with this method we can send parameters too.
    'location': (None, 'HUN'),
    'maxreads': (None, 1),
    'service': (None, 'ANPR'),
}

# The request were made here. 
# In the headers variable we provide the API key, the files variable will contain the
# recently made multipart_data dictionary.
resp = requests.post('https://api-us.anpr-cloud.com/free',
                     files=multipart_data,
                     headers={'X-Api-Key' : '5HdorOqjNq5sgi0D9Ik1Z8DyTccsK6TVaw16e0Tj'})

# The json.loads method parses the REST API response text part 
# into a python dictionary object
resp_dict = json.loads(resp.text)

# Print the results
print(f"The Response JSON raw text: {resp.text}")

print(f"The parsed dictionary's content: {resp_dict}")