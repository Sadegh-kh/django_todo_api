# Generated by Django 4.2.4 on 2023-08-27 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date_do', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]