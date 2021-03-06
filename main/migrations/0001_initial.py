# Generated by Django 3.1.2 on 2020-10-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=100)),
                ('itemquantity', models.CharField(max_length=100)),
                ('itemstatus', models.CharField(choices=[('PENDING', 'PENDING'), ('BOUGHT', 'BOUGHT'), ('NOT AVAILABLE', 'NOT AVAILABLE')], max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]
