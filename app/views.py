from django.shortcuts import render
from .models import Member, Student
from .models import Player
from .models import Caddie
from rest_framework import generics
from .serializers import PlayerSerializer
# Create your views here.
def index(request): #function names index that is called when a user visits my hompage
    #1. this checks ifthe url has a query paramter example: http://127.0.0.1:8000/?q=student
    query  = request.GET.get('q')
    #
    #2. if query is not empty this line runs, Student.objects.filter()  this is how we fetch records from the database that match a condition,
    #  -> name__icontains=query means : give me all student objects where the name conains the search word example john will match john or johnny
    if query:
        obj = Student.objects.filter(name__icontains=query)
    else:
        obj = Student.objects.all()
    #if no search query is provided it just fetches all students
    #
    #3. this is a dictonary that stores data we want to send to to the html template , we use obj in the template index.html to loop through and show the students
    context = {
        "obj" : obj,
    }
    #
    #4. this tells django to use index.html and pass it to the context dictonary to the template has students to display
    return render(request, "index.html", context)

#lets make a view so we can see the baseball players
def baseball_players(request):
    # fetch the players and from the database
    players = Player.objects.all()
    # pass the to the template
    context = {
        "players" : players,
    }
    #this tells django to use baseball_players.html and pass it to the context dictonary to the template has players to display
    return render(request, "baseball_page.html", context)


# 4/26    lets create a view for the api endpoint to list players
# generic view by django's rest framwrok make to handle get requests serialized in a json
class PlayerListAPIView(generics.ListAPIView):
    # tells the view get all player objects from the db
    queryset = Player.objects.all()
    # below tells user PlayerSeralizer to convert eac players to jscon
    serializer_class = PlayerSerializer
    #


#lets make a view so we can see the caddies
def caddies(request):
    # fetch the caddies and from the database
    caddies = Caddie.objects.all()
    # pass the to the template
    context = {
        "caddies" : caddies,
    }
    #this tells django to use cadddie_players.html and pass it to the context dictonary to the template has caddies to display
    return render(request, "caddie_page.html", context)


#lets make a view so we can see the members at our clun
def members_view(request):
    # fetch the members  and from the database
    members = Member.objects.all()
    # pass the to the template
    context = {
        "members" : members,
    }
    #this tells django to use cadddie_players.html and pass it to the context dictonary to the template has caddies to display
    return render(request, "members_page.html", context)