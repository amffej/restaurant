# Generated by Django 2.2.3 on 2019-07-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entree',
            name='addons',
            field=models.ManyToManyField(blank=True, null=True, to='orders.Addon'),
        ),
    ]
