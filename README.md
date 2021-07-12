# url_shortner_api
url_shortner_api is RESTApi written using django &amp; django rest framework that is used to shorten the long input urls

How to run as a django application:-
1. git clone https://github.com/nishant-passari/url_shortner_api.git
2. cd url_shortner_api/url_shortner/
3. python manage.py runserver
4. You can access the application by typing 127.0.0.1:8000/ in your browser's address bar
5. Click on the link 127.0.0.1:8000/shortner


How to run as a docker container:-
1. Make sure you have docker running in your machine.
2. Execute:-
   docker run -p 7521:7521 -t nishant195/testapi:v1

Happy converting long URLs to short URLs.
