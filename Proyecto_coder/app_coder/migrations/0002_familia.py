# Generated by Django 4.0.4 on 2022-05-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField()),
                ('cadena', models.CharField(max_length=40)),
            ],
        ),
    ]
