from django.urls import path,re_path, include

from . import views

urlqme = [
path('', views.all, name = 'listqme'),
re_path(r'(?P<name>[A-Z][^/]+)$', views.selectqme, name ='link'),
re_path(r'(?P<nameservice>[A-Z][^/]+)/new', views.newservice, name ='newservice')

]

urlpatterns = [
	path('', views.index, name = 'firstday'),
	path('all',views.all, name = 'all'),
	path('dataview' ,views.dataview, name = 'dataview'),
	path('firstday' ,views.firstday, name = 'firstday'),
	path('secondday' ,views.secondday, name = 'secondday'),
	path('rating' ,views.rating, name = 'rating'),

	path('listqme/', include (urlqme))
	
]
