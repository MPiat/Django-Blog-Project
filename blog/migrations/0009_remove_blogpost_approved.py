# Generated by Django 2.0.2 on 2018-03-02 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogpost_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='approved',
        ),
    ]