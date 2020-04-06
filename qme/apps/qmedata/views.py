from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import DataForm, SerchForm, ServiceForm, EquipmentForm
from .models import Equipment, Measurements, Calibr, Deviations, Service
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
			context = show(None)
			return render(request, 'qmedata/listqme.html',{'context':context})
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
		comparision(MyData)
		MyData.save()
				

def comparision(data_equipment):
	rating = data_equipment.equipment.rating
	if data_equipment.equipment.group_weight == False:
		difference = abs(round(float(data_equipment.weight) - Calibr.objects.get(calibr_name="Индивидуальный вес").value_calibr,3 ))
		abs(difference)
		if difference > Deviations.objects.get(pk=1).dev_ind_weight:
			rating = rating + 1	
	else:
		difference = abs(round(float(data_equipment.weight) - Calibr.objects.get(calibr_name="Групповой вес").value_calibr,3 ))
		
		if difference > Deviations.objects.get(pk=1).dev_grp_weight:
	 		rating = rating + 1	
	#print (rating)
	if data_equipment.equipment.this_is_sdl == True:
		difference = abs(round(float(data_equipment.size_one) - Calibr.objects.get(calibr_name="SizeSdl").value_calibr,3 ))
		if difference > Deviations.objects.get(pk=1).dev_sdl_size:
			rating = rating + 1
	else:
		difference = abs(round(float(data_equipment.size_one) - Calibr.objects.get(calibr_name="SizeOne").value_calibr,2 ))
		if difference > Deviations.objects.get(pk=1).dev_one_size:
			rating = rating + 1

	if data_equipment.size_two != None:
		difference = abs(round(float(data_equipment.size_two) - Calibr.objects.get(calibr_name="SizeTwo").value_calibr,2 ))
		if difference > Deviations.objects.get(pk=1).dev_two_size:
			rating = rating + 1

	if data_equipment.equipment.type_equipment == 'Cig':
		difference = abs(round(float(data_equipment.airPD) - Calibr.objects.get(calibr_name="PD Cig").value_calibr,0 ))
		if difference > Deviations.objects.get(pk=1).dev_sig_pd:
			rating = rating + 1
	if data_equipment.equipment.type_equipment == 'Filter':

		difference = abs(round(float(data_equipment.airPD) - Calibr.objects.get(calibr_name="PD filter").value_calibr,0 ))
		if difference < 122:
			if difference > Deviations.objects.get(pk=1).dev_fil_pd:
				rating = rating + 1
		else:
			difference = abs(round(float(data_equipment.airPD) - Calibr.objects.get(calibr_name="HighPD").value_calibr,0 ))
			if difference > Deviations.objects.get(pk=1).dev_fil_pd:
				rating = rating + 1

	if data_equipment.airVent != None:
		difference = abs(round(float(data_equipment.airVent) - Calibr.objects.get(calibr_name="Vent").value_calibr,1 ))
		if difference > Deviations.objects.get(pk=1).dev_vent:
			rating = rating + 1

	if data_equipment.equipment.rating != rating:
		Equipment.objects.filter(pk=data_equipment.equipment.id).update(rating = rating)
		print (Equipment.objects.get(pk=data_equipment.equipment.id).rating)
	






def firstday(request):
	
	if request.user.is_authenticated == True:
		if request.method == 'GET':
			a='First'
			context = show(a)
			text="первый день"
			return render(request, 'qmedata/list.html',{'context':context, 'text':text})
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
			text="второй день"
			return render(request, 'qmedata/list.html',{'context':context, 'text':text})
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

		form_data = Measurements.objects.filter(equipment=index_equipment).order_by('-data_messure')
						

		#messages.success(request, 'Данные представлены')
		
		
		return render(request, 'qmedata/dataview.html', {'form':form, 'form_data':form_data})
		#return redirect(reverse('dataview'))
	
	
	if request.method == 'GET':
		if request.user.is_authenticated == True:

			return render(request, 'qmedata/dataview.html', {'Message':Message, 'form':form}  )
		else:
			return redirect('/accounts/login/')	

def rating(request):

	if request.method == 'GET':
		if request.user.is_authenticated == True:
			Message = "Антирейтинг"
			rating = Equipment.objects.all().order_by('-rating')

			return render(request, 'qmedata/rating.html', {'Message':Message, 'Rating':rating})
		else:
			return redirect('/accounts/login/')	


def show(a):
	
	
	if a == None:
		
	
		
		for b in Equipment.objects.all():
			if b.count_service != Equipment.objects.filter(service__equipment=b.id).count():		
				b.count_service = Equipment.objects.filter(service__equipment=b.id).count()		
			
				b.save()
			#print(Service.objects.filter(equipment=b.id).count())
		

		list_equipment = Equipment.objects.all().order_by('-no_workability', 'equipment_name',)


		
		context = list_equipment
	else:
		list_equipment = Equipment.objects.filter(place_equipment=a).order_by('equipment_name')
		context = [DataForm(x, x.id) for x in list_equipment]
	return (context)


def selectqme(request, name):
	if request.method == 'POST':
		print("Кнопка нажата")

	selectqme = name
	#Equipment.objcets.only('selectqme')
	

	objects_qme = Equipment.objects.get(equipment_name=selectqme)
	list_service = Service.objects.filter(equipment=Equipment.objects.get(equipment_name=selectqme)).order_by('-data_messure')
	return render(request, 'qmedata/qmeselect.html', {'qmename':selectqme, 'list_service':list_service, 'qme':objects_qme})





def newservice(request, nameservice):
	selectqme = nameservice
	objects_qme = Equipment.objects.get(equipment_name=selectqme)
	if request.user.is_authenticated == True:
		if request.method == 'GET':
		

	
	#form=ServiceForm()
			form=ServiceForm()
			form_notwork = EquipmentForm(initial={'no_workability':objects_qme.no_workability})
			return render(request, 'qmedata/newservice.html', {'qme':objects_qme, 'form':form, 'form_notwork': form_notwork})
		if request.method == 'POST':
			
			s=ServiceForm(request.POST)
			data_service = s.save(commit=False)
			data_service.equipment = objects_qme
			data_service.name_user = request.user
			data_service.save()
			messages.success(request, 'Данные сохранены')

			q=EquipmentForm(request.POST, instance = objects_qme )
			q.save()
		
			return redirect('newservice', nameservice=selectqme)
	else:
		return redirect('/accounts/login/')	


def editservice(request, nameservice, service_id):
	
	service_objects = Service.objects.get(pk = service_id)
	objects_qme = Equipment.objects.get(equipment_name=service_objects.equipment)

	if request.user.is_authenticated == True:
		if request.method == 'GET':
			#objects_qme = Equipment.objects.get(equipment_name=nameservice)
			
			
			form=ServiceForm(instance = service_objects)
			form_notwork = EquipmentForm(initial={'no_workability':objects_qme.no_workability})
			return render(request, 'qmedata/editservice.html', {'form':form, 'form_notwork':form_notwork, 'qme':objects_qme, 'service':service_objects})
		 



		if request.method == 'POST':
			if request.POST.getlist('delete') != ['delete']:
				s=ServiceForm(request.POST, instance = service_objects)
				s.save()
				q=EquipmentForm(request.POST, instance = objects_qme )
				q.save()
				messages.success(request, 'Данные сохранены')
				return redirect('editservice', nameservice=nameservice, service_id=service_id)
			else:
				
				service_objects.delete()
			return redirect('newservice', nameservice=nameservice)
			
		

			

	else:
		return redirect('/accounts/login/')	


def allservice(request):

	list_service = Service.objects.all().order_by('-it_is_no_ok', '-data_messure')

	return render(request, 'qmedata/allservice.html', {'form':list_service})
