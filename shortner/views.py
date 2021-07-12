from rest_framework.response import Response
from . serializers import ShortnerSerializer
from rest_framework import viewsets, status
import json
import random
from django.conf import settings

class UrlShortner(viewsets.ViewSet):
    """Reduces the length of long URLs.

    Input the long url in json format:
    Example:-
    {"url": "https://www.infracloud.io/blogs/avoiding-kubernetes-cluster-outages-synthetic-monitoring/"}

    You will get the short url as a response.
    """
    path = settings.BASE_DIR + '/shortner/mapper.txt'

    def url_generator(self, url, json_data):
        """The url_generator method generates a short url 
        corresponding to the long url given as input and returns
        short_url.
        """
        new_str = ''
        for i in range(5):
            j = random.randint(0, len(url)-1)
            if url[j] in ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','[',']',
            '{','}',':',';','"',"'",',','<','>','.','?','/','\\','|','`','~']:
                new_str += str(random.randint(0,8))
            else:
                new_str += random.choice([url[j].upper(), url[j].lower()])
        
        # Calling url_generator() again if the short url
        # generated is already used by some other long url.
        if new_str in json_data.values():
            self.url_generator(url, json_data)
        return 'example.ly/' + new_str

    def create(self, request):
        """The create method here first checks if the URL starts with
        'http://' or not. If not, the method will concatenate 'http://'
        at the starting of the URL so that the shortner API functions
        properly. This is just to overwrite the functionality of default
        validator of the URLField used in serializer.py file.
        """
        data = request.data
        if 'www.' in data['url'][:4]:
            data['url'] = "http://" + data['url']

        serializer = ShortnerSerializer(data=data)
        url = request.data.get('url')
        if serializer.is_valid():
            with open(UrlShortner.path) as fh:
                json_data =  json.load(fh)
            
            # Checking if the long_url is already present as keys in
            # the text file. If present, returns the corresponding
            # short_url instead of generating a new one.
            if url in json_data.keys():
                return Response({'short_url': json_data[url]}, status=status.HTTP_200_OK)
            
            # If not present, generate a new short url.
            else:
                short_url = self.url_generator(url, json_data)    
                new_dict = {url : short_url}
                json_data.update(new_dict)
                
                # Writing {"long_url":"short_url"} in a text file so that the user
                # gets the same short_url as it gave before instead of generating
                # a new one.
                with open(UrlShortner.path,'w') as fh:
                    json.dump(json_data, fh)

            return Response({'short_url':short_url}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
