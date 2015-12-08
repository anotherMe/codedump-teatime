
from django.db import models
from django.conf import settings



def get_pin_path(pin_instance, filename):
	return 'pins/{0}/{1}'.format(pin_instance.sample.id, filename)

 
class Shop(models.Model):
	
	name = models.CharField(max_length=200)
	url = models.URLField(max_length=200)

	def __str__(self):
		return self.name
		

class Sample(models.Model):
	
	name = models.CharField(max_length=200)
	altName = models.CharField('alternative name', max_length=200)
	descr = models.TextField('Description')
	rating = models.IntegerField(default=0)
	shop = models.ForeignKey(Shop)
	addDate = models.DateField('date added')

	def __str__(self):
		return self.name


class Pin(models.Model):
	
	#~ img = models.ImageField(upload_to='pins/')
	img = models.ImageField(upload_to=get_pin_path)
	sample = models.ForeignKey(Sample)
	isCoverImage = models.BooleanField(default=False)

