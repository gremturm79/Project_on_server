# Generated by Django 4.1.7 on 2023-06-10 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_1', '0010_myobject_date_alter_myobject_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationObjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bind', models.ManyToManyField(to='main_1.myobject')),
            ],
        ),
    ]
