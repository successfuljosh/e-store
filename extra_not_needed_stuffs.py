# run all the code via the terminal
# python manage.py shell
from django.contrib.sessions.models import Session
s= Session.objects.get(pk='1wfkflefcuk15j8z6qufdc90dok5a4lq')
s.get_decoded()