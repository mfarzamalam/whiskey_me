# Generated by Django 3.2.8 on 2021-12-28 18:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('age', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('product_stripe_id', models.CharField(blank=True, max_length=100, null=True)),
                ('product_price_is_subscribe_id', models.CharField(blank=True, max_length=100, null=True)),
                ('product_price_not_subscribe_id', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]
