from django.db import models


class Equipment(models.Model):
	equipment_name = models.CharField('название', max_length=30)
	group_weight = models.BooleanField()
	this_is_sdl = models.BooleanField()
	type_equipment_choices = (('Cig','Измеряет сигареты'),('Filter','Измеряет фильтра'))
	type_equipment = models.CharField('Тип измерений', max_length=6, choices=type_equipment_choices)
	place_equipment_choices = (('First','Первый день'),('Second','Второй день'),('NoActive','Не активна'))
	place_equipment = models.CharField('Калибровочный день', max_length=30, choices=place_equipment_choices)
	rating = models.IntegerField(default=0)
	count_service = models.IntegerField(default=0)

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


class Deviations(models.Model):
	dev_ind_weight = models.FloatField(default=0.005)
	dev_grp_weight = models.FloatField(default=0.009)
	dev_sdl_size = models.FloatField(default=0.004)
	dev_one_size = models.FloatField(default=0.04)
	dev_two_size = models.FloatField(default=0.04)
	dev_sig_pd = models.FloatField(default = 4)
	dev_fil_pd = models.FloatField(default = 8)
	dev_vent = models.FloatField(default = 1)

	def __str__(self):
		return str("Отклонения")

	class Meta:
		verbose_name = 'Отклонение'
		verbose_name_plural = 'Отклонения'



class Service(models.Model):
	equipment = models.ForeignKey(Equipment, on_delete = models.CASCADE)
	name_problem = models.CharField('Проблема', max_length=100)
	description_service = models.CharField('Описание ремонта', max_length=1000)
	spare_parts_required = models.CharField('Требующиеся запчасти', max_length=300 , blank = True)
	it_is_no_ok = models.BooleanField()
	name_user = models.CharField(max_length=30)
	data_messure = models.DateField()
	
	def __str__(self):
		template = '{0.equipment} {0.name_problem}'
		return template.format(self)



	class Meta:
		verbose_name = 'Сервис'
		verbose_name_plural = 'Сервис'
		