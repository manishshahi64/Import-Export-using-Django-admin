# Generated by Django 3.1 on 2021-03-16 21:10

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210317_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='Address',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='City',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Company_Name',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Contact_Name',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Contact_Title',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Country',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Email',
            field=models.EmailField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Fax',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='First_Name',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Industry_Type',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Last_Name',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Phone',
            field=phone_field.models.PhoneField(blank=True, default='NaN', max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='State',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Total_Employees',
            field=models.CharField(blank=True, default='NaN', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Url',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='Zip',
            field=models.CharField(blank=True, default='NaN', max_length=100, null=True),
        ),
    ]