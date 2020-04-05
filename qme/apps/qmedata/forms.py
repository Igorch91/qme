from django import forms
from .models import Equipment,Calibr, Service

from django.forms import ModelForm



class DataForm(forms.Form):

	equipment_name = forms.CharField(max_length=30)
	weight_value = forms.FloatField()
	size_one_value = forms.FloatField()
	size_two_value = forms.FloatField()
	airPd_value = forms.IntegerField()
	airVent_value = forms.FloatField()

	def __init__ (self, equipment, id_equipment, **kwargs):
		super().__init__()
		self.prefix=id_equipment
		self.fields["equipment_name"].initial=equipment
		self.fields["equipment_name"].label=equipment
		if equipment.group_weight == True:
			self.fields["weight_value"].initial=Calibr.objects.get(calibr_name="Групповой вес").value_calibr
		else:
			self.fields["weight_value"].initial=Calibr.objects.get(calibr_name="Индивидуальный вес").value_calibr
		self.fields["weight_value"].widget.attrs['style'] = "width:60px"
		if equipment.this_is_sdl == True:
			self.fields["size_one_value"].initial=Calibr.objects.get(calibr_name="SizeSdl").value_calibr
			self.fields["size_two_value"].initial=None
		else:
			self.fields["size_one_value"].initial=Calibr.objects.get(calibr_name="SizeOne").value_calibr
			self.fields["size_two_value"].initial=Calibr.objects.get(calibr_name="SizeTwo").value_calibr
		self.fields["size_one_value"].widget.attrs['style'] = "width:80px"
		self.fields["size_two_value"].widget.attrs['style'] = "width:80px"
		if equipment.type_equipment == 'Cig':
			self.fields["airPd_value"].initial=Calibr.objects.get(calibr_name="PD Cig").value_calibr
			self.fields["airVent_value"].initial=Calibr.objects.get(calibr_name="Vent").value_calibr
		else:
			self.fields["airPd_value"].initial=Calibr.objects.get(calibr_name="PD filter").value_calibr
			self.fields["airVent_value"].initial=None
			self.fields["airVent_value"].disabled=True
		self.fields["airPd_value"].widget.attrs['style'] = "width:60px"
		self.fields["airVent_value"].widget.attrs['style'] = "width:60px"

		

class SerchForm(forms.Form):
	 equipment = forms.ModelChoiceField( queryset=Equipment.objects.all().order_by('equipment_name'))


class DateInput(forms.DateInput):
	input_type = 'date'


class ServiceForm(forms.ModelForm):
	
	#checkin = forms.DateField(widget=DateInput())
	class Meta:
		model = Service
		widgets = { 
            'description_service': forms.Textarea(attrs={'rows':15, 'cols':53}),
        	'spare_parts_required': forms.Textarea(attrs={'rows':5, 'cols':53}),
        	'name_problem':forms.TextInput(attrs={'size':'61'}),
        	'data_messure': DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        } 



		fields =['name_problem','description_service', 'spare_parts_required', 'it_is_no_ok', 'data_messure']
		#['equipment','name_problem','description_service','spare_parts_required','it_is_no_ok','name_user','data_messure']

class EquipmentForm(forms.ModelForm):
	class Meta:
		model = Equipment

		fields = ['no_workability']