# Generated by Django 2.1.4 on 2018-12-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('passowrd', models.CharField(max_length=5000)),
                ('web', models.CharField(blank=True, max_length=200)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('photo', models.ImageField(default='https://i.kinja-img.com/gawker-media/image/upload/s--rjyuIlzA--/c_scale,f_auto,fl_progressive,q_80,w_800/hpfeqdnehtcjbplrvqkl.jpg', upload_to='')),
                ('birthday', models.DateTimeField(blank=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
