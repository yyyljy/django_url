from django.shortcuts import render
import random
import requests

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def favorite(request, name):
    foods = ['짜장면','탕수육','피자','치킨','초밥','파이타','국밥']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'name' : name
    }
    return render(request, 'pages/favorite.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'pages/catch.html', context)

def buy(request):
    return render(request, 'pages/buy.html')

def lotto(request):
    cnt = request.GET.get('cnt')
    
    picks = []
    for i in range(int(cnt)):
        numbers = random.sample(range(1,46),6)
        numbers.sort()
        picks.append(numbers)

    sorted_lottos = sorted(numbers)
    sort_lottos = numbers.sort()
    context = {
        'picks' : picks,
        'sorted_lottos' : sorted_lottos,
        'sort_lottos' : sort_lottos
    }
    return render(request, 'pages/lotto.html', context)


def artii(request):
    return render(request, 'pages/artii.html')

def result(request):
    msg = request.GET.get('message')
    result = requests.get(f'http://artii.herokuapp.com/make?text={msg}').text
    context = {
        'result' : result
    }
    return render(request, 'pages/result.html', context)