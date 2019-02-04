# Generated by Django 2.0.10 on 2019-02-04 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='博客标签')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='博客分类')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
    ]