# Generated by Django 3.2.4 on 2021-06-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectfee', '0011_alter_applicationform_annualincome'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationform',
            name='result1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='result2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='result3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='result4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='result5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='result6',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
