from __future__ import unicode_literals

from django.db import models

# Create your models here.
class members(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	newsletter = models.IntegerField(default=1)
	is_adm = models.IntegerField(default=0)
	company_id = models.IntegerField(default=0)

	def __first_name__(self):
		return self.first_name

	def __last_name__(self):
		return self.last_name

	def __email__(self):
		return self.email

	def __phone__(self):
		return self.phone

	def __created_at__(self):
		return self.created_at

	def __newsletter__(self):
		return self.newsletter

	def __is_adm__(self):
		return self.is_adm

class company(models.Model):
	company_name = models.CharField(max_length=400)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	cnpj = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	zip_code = models.CharField(max_length=200)
	address = models.CharField(max_length=200)

	def __company_name__(self):
		return self.company_name

	def __email__(self):
		return self.email

	def __phone__(self):
		return self.phone

	def __cnpj__(self):
		return self.cnpj

	def __created_at__(self):
		return self.created_at

	def __zip_code__(self):
		return self.zip_code

	def __address__(self):
		return self.address