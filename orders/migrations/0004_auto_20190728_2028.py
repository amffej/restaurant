# Generated by Django 2.2.3 on 2019-07-29 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_size_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(help_text='Max of 250 Characters', max_length=250)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in $US', max_digits=6)),
                ('addon_free', models.BooleanField(default=True)),
                ('addonLimit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.AddonLimit')),
            ],
        ),
        migrations.AddField(
            model_name='addon',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Price in $US', max_digits=6),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Entree',
        ),
        migrations.AddField(
            model_name='item',
            name='addons',
            field=models.ManyToManyField(blank=True, null=True, to='orders.Addon'),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Category'),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
    ]
