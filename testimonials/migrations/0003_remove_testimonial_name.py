# Generated by Django 3.2.25 on 2024-06-24 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_alter_testimonial_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='name',
        ),
    ]
