from django.urls import path,re_path

from . import views


urlpatterns = [
	path('', views.index, name = 'firstday'),
	path('all',views.all, name = 'all'),
	path('dataview' ,views.dataview, name = 'dataview'),
	path('firstday' ,views.firstday, name = 'firstday'),
	path('secondday' ,views.secondday, name = 'secondday'),
	path('rating' ,views.rating, name = 'rating'),
	path('listqme',views.all, name = 'listqme'),
	re_path(r'[A-Z&_&0-9]{6,}$', views.selectqme, name ='link')
]
