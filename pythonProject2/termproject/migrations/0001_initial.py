# Generated by Django 4.2.3 on 2023-08-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('op_1', models.CharField(max_length=200)),
                ('op_2', models.CharField(max_length=200)),
                ('op_3', models.CharField(max_length=200)),
                ('op_4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
    ]
