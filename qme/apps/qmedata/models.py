from django.db import models


class Equipment(models.Model):
	equipment_name = models.CharField('название', max_length=30)
	group_weight = models.BooleanField()
	this_is_sdl = models.BooleanField()
	type_equipment_choices = (('Cig','Измеряет сигареты'),('Filter','Измеряет фильтра'))
	type_equipment = models.CharField('Тип измерений', max_length=6, choices=type_equipment_choices)
	place_equipment_choices = (('First','Первый день'),('Second','Второй день'))
	place_equipment = models.CharField('Калибровочный день', max_length=30, choices=place_equipment_choices)
	
	def __str__(self):
		return self.equipment_name

	class Meta:
		verbose_name='Оборудование'
		verbose_name_plural = 'Оборудование'
		unique_together = ['equipment_name']

class Measurements(models.Model):
	equipment = models.ForeignKey(Equipment, on_delete = models.CASCADE)
	weight = models.FloatField(blank = True)
	size_one = models.FloatField(blank = True)
	size_two = models.FloatField(blank = True, null = True)
	airPD = models.FloatField(blank = True)
	airVent = models.FloatField(null = True, blank = True)
	data_messure = models.DateField()
	time_messure = models.TimeField()
	name_user = models.CharField(max_length=30)

	def __str__(self):
		return str(self.equipment)

	class Meta:
		verbose_name = 'Измерение'
		verbose_name_plural = 'Измерения'

class Calibr(models.Model):
	calibr_name = models.CharField('Калибр' , max_length=30)
	value_calibr = models.FloatField()

	def __str__(self):
		return str(self.calibr_name)

	class Meta:
		verbose_name = 'Калибр'
		verbose_name_plural = 'Калибры'
		unique_together = ['calibr_name']


