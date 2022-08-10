from django.urls import path

from api_app import views

urlpatterns = [
    path('', views.index, name='nwindex'),
    path('evolution/<int:id>', views.evolution, name='nwevolution'),
    path("search/<name>", views.search, name="nwsearch"),
    path('ping/', views.ping, name="nwhello"),
]