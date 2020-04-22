# Generated by Django 2.2.10 on 2020-04-21 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catogary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('D', 'draft'), ('p', 'published')], max_length=1)),
                ('image', models.ImageField(blank=True, upload_to='blog/post')),
                ('Catogary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.Catogary')),
            ],
        ),
    ]
