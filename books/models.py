from django.db import models

class Publisher(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50 ,blank=True)
	city=models.CharField(max_length=60 ,blank=True)
	state_province=models.CharField(max_length=20,blank=True)
	country=models.CharField(max_length=30,blank=True)
	website=models.URLField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-name']
		


class Author(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	email=models.EmailField(blank=True, verbose_name='e-mail')

	def __str__(self):
		return u'%s %s' %(self.first_name, self.last_name)

class Book(models.Model):
	title=models.CharField(max_length=100)
	author=models.ManyToManyField(Author)
	publisher=models.ForeignKey(Publisher, on_delete="CASCADE")
	publication_date=models.DateField(blank=True)

	def __str__(self):
		return self.title




