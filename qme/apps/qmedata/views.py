from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import DataForm, SerchForm
from .models import Equipment, Measurements, Calibr
from django.contrib import messages
from django.urls import reverse
from django.utils.formats import sanitize_separators
from django.utils.timezone import now

# Create your views here.
def index(request):
	
	return redirect('all')


def all(request):
	if request.user.is_authenticated == True:
		if request.method == 'GET':
			a='First'
			context = show(None)
			return render(request, 'qmedata/list.html',{'context':context})
	else:
		return redirect('/accounts/login/')
	if request.method == 'POST':
		savedata(request.POST, request.user)
		messages.success(request, 'Данные сохранены')
		return redirect(reverse('all'))



def savedata(content, user):
	print(content)
	dict_creat = content.dict()

	dict_creat.pop('csrfmiddlewaretoken',None)
	dict_creat.pop('data',None)

	x=dict_creat.keys()

	id_equipment=list()

	for y in x:
		s = str(y)
		z=s.split("-")
		id_equipment.append(z[0])

	unik_id=sorted(list(set(id_equipment)))
	print(unik_id)

	for i in unik_id:
		MyData = Measurements()
		MyData.equipment=Equipment.objects.get(equipment_name= dict_creat.get(str(i)+"-"+'equipment_name'))
		MyData.weight=sanitize_separators(dict_creat.get(str(i)+"-"+'weight_value'))
		MyData.size_one=sanitize_separators(dict_creat.get(str(i)+"-"+'size_one_value'))
		MyData.size_two=sanitize_separators(dict_creat.get(str(i)+"-"+'size_two_value'))
		MyData.airPD=sanitize_separators(dict_creat.get(str(i)+"-"+'airPd_value'))
		MyData.airVent=sanitize_separators(dict_creat.get(str(i)+"-"+'airVent_value'))
		MyData.data_messure = now()
		MyData.time_messure = now()
		MyData.name_user = user
		
		MyData.save()
				
def firstday(request):
	
	if request.user.is_authenticated == True:
		if request.method == 'GET':
			a='First'
			context = show(a)
			return render(request, 'qmedata/list.html',{'context':context})
	else:
		return redirect('/accounts/login/')
	if request.method == 'POST':
		savedata(request.POST, request.user)
		messages.success(request, 'Данные сохранены')
		return redirect(reverse('firstday'))

def secondday(request):
	
	if request.user.is_authenticated == True:
		if request.method == 'GET':
			a='Second'
			context = show(a)
			return render(request, 'qmedata/list.html',{'context':context})
	else:
		return redirect('/accounts/login/')
	if request.method == 'POST':
		savedata(request.POST, request.user)
		messages.success(request, 'Данные сохранены')
		return redirect(reverse('secondday'))


		
def dataview(request):

	Message = "База данных"	
	form = SerchForm()

	if request.method == 'POST':
		
		index_equipment_dict =request.POST.dict()
		index_equipment = index_equipment_dict.get('equipment')

		form_data = Measurements.objects.filter(equipment=index_equipment).order_by('-data_messure').order_by('-time_messure')
						
		


		messages.success(request, 'Данные представлены')
		
		
		return render(request, 'qmedata/dataview.html', {'Message':Message, 'form':form, 'form_data':form_data})
		#return redirect(reverse('dataview'))
	
	
	if request.method == 'GET':
		if request.user.is_authenticated == True:

			return render(request, 'qmedata/dataview.html', {'Message':Message, 'form':form}  )
		else:
			return redirect('/accounts/login/')	

def show(a):
	#print(a)
	if a == None:
		list_equipment = Equipment.objects.all().order_by('equipment_name')
	else:
		list_equipment = Equipment.objects.filter(place_equipment=a).order_by('equipment_name')
	context = [DataForm(x, x.id) for x in list_equipment]
	return (context)
