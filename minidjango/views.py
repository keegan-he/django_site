import requests
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     # This is similar to ones we have done before. Instead of keeping
#     # the HTML / template in a separate directory, we just reply with
#     # the HTML embedded here.
#     return HttpResponse('''
#         <h1>Welcome to my home page!</h1>
#         <a href="about">About me</a> <br />
#         <a href="photography">photography</a> <br />
#         <a href="/github-api-example">See my GitHub contributions</a> <br />
#     ''')


def about_me(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'name': 'Ash Ketchum',
        'pokemon': 'Pikachu',
    }
    return render(request, 'about_me.html', context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/keegan-he/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)


def about(request):
    content_html = open('content/about.html').read()
    context = {
        'about': content_html,
    }
    return render(request,'base.html', context)

def photography(request):
    content_html = open('content/photography.html').read()
    context = {
        'photography': content_html, 
    }
    return render(request, 'base.html', context)

def projects(request):
    content_html = open('content/projects.html').read()
    context = {
        'projects': content_html, 
    }
    return render(request, 'base.html', context)

def contact(request):
    content_html = open('content/contact.html').read()
    context = {
        'contact': content_html, 
    }
    return render(request, 'base.html', context)

def index(request):
    content_html = open('content/index.html').read()
    context = {
        'index': content_html, 
    }
    return render(request, 'base.html', context)