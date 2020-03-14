# Generated by Django 3.0.3 on 2020-03-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField()),
                ('materials', models.ManyToManyField(related_name='lessons', to='lesson.Material')),
            ],
        ),
    ]