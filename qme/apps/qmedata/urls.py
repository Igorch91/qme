from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name = 'index'),
	path('all',views.all, name = 'all'),
	path('dataview' ,views.dataview, name = 'dataview'),
	path('firstday' ,views.firstday, name = 'firstday'),
	path('secondday' ,views.secondday, name = 'secondday'),
	path('rating' ,views.rating, name = 'rating')
]
