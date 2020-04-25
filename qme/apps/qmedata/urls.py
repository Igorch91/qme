from django.urls import path,re_path, include


from . import views

urlservice = [
re_path(r'(?P<service_id>\d+)', views.editservice, name='editservice')
#re_path(r'(?P<delete_id>\d+)/delete', views.delete, name='delete')

	]


urlqme = [
path('', views.all, name = 'listqme'),
re_path(r'(?P<name>[A-Z][^/]+)$', views.selectqme, name ='link'),

re_path(r'(?P<nameservice>[A-Z][^/]+)/new', views.newservice, name ='newservice'),
re_path(r'(?P<nameservice>[A-Z][^/]+)/', include (urlservice))
]

urlpatterns = [
	path('', views.index, name = 'firstday'),
	path('all',views.all, name = 'all'),
	path('dataview' ,views.dataview, name = 'dataview'),
	path('firstday' ,views.firstday, name = 'firstday'),
	path('secondday' ,views.secondday, name = 'secondday'),
	path('rating' ,views.rating, name = 'rating'),
	path('allservice' ,views.allservice, name = 'allservice'),
	path('listqme/', include (urlqme)),
	path('test', views.test, name = 'test')
	
]
