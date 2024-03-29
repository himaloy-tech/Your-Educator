# Generated by Django 3.0.7 on 2020-10-24 02:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Desc', models.TextField()),
                ('Category', models.CharField(choices=[('Speaking Language', 'Speaking Language'), ('Computer Engineering', 'Computer Engineering'), ('Bussiness Studies', 'Bussiness Studies'), ('Sceince', 'Sceince'), ('History', 'History')], max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('img', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blogcomment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countrycode', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('subject', models.TextField(blank=True, null=True)),
                ('message', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Motivational_Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
