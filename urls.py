from django.urls import path

import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.index),
    path('about_me', views.about_me),
    path('about', views.about),
    path('photography', views.photography),
    path('projects', views.projects),
    path('contact', views.contact),
    path('index', views.index),
    path('music', views.music),
    path('github-api-example', views.github_api_example),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

