from django.urls import path
from store import views
from store.views import news

urlpatterns = [

    path('', news, name='news'),
    path("news/", views.news, name='news'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path('news/<int:id>/', views.single, name='single'),
]
