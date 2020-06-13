from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')

def favorite(request, name):
    foods = ['짜장면','탕수육','피자','치킨','초밥','파이타','국밥']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'name' : name
    }
    return render(request, 'favorite.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'catch.html', context)

def buy(request):
    return render(request, 'buy.html')

def lotto(request):
    cnt = request.GET.get('cnt')
    
    picks = []
    for i in range(int(cnt)):
        numbers = random.sample(range(1,46),6)
        numbers.sort()
        picks.append(numbers)
    context = {
        'picks' : picks
    }
    return render(request, 'lotto.html', context)