from django.db import models
from phone_field import PhoneField

class Database(models.Model):
	
	Email=models.EmailField(max_length=100,blank=True,null=True,default="NaN")
	Technology_Type=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	Company_Name=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	Url=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	Contact_Name=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	First_Name=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	Last_Name=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	Contact_Title=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	Address=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	City=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	State=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	Zip=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	Country=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	Phone = PhoneField(blank=True,null=True,default="NaN")
	Fax=models.CharField(max_length=100,blank=True,null=True,default="NaN")
	Total_Employees=models.CharField(max_length=50,blank=True,null=True,default="NaN")
	Industry_Type=models.CharField(max_length=100,blank=True,null=True,default="NaN")

	# title = models.CharField(max_length=120)
	# author = models.CharField(max_length=120)
	# content = models.TextField()
	def __str__(self):
		return self.Industry_Type
