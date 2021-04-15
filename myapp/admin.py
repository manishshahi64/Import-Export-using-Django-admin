from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Database
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ExportActionMixin

class DataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	# list_display = ['title', 'author', 'content']
	list_display = ['Email','Technology_Type','Company_Name', 'Url','Contact_Name','Contact_Title','Address','City','State','Zip','Country','Phone','Fax','Total_Employees','Industry_Type']
	search_fields = ('Email', 'Technology_Type', 'Company_Name', 'Url','Contact_Name','First_Name','Last_Name','Contact_Title','Address','City','State','Zip','Country','Phone','Fax','Total_Employees','Industry_Type')
	list_filter=('Industry_Type','State','Technology_Type','Country','Contact_Title',)
admin.site.register(Database, DataAdmin)