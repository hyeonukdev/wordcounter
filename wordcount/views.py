from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') 
    #render 세게의 인자 1.request 2template인자 3.사전형객체,딕셔너리형객체

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split() #공백기준으로 나눠줌, 리스트가됨
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1 
        else:
            #add to dictonary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : word_dictionary.items()})