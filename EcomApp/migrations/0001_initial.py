# Generated by Django 5.0.4 on 2024-04-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('mobile', 'Mobile'), ('laptop', 'Laptop'), ('Tv', 'TV')], max_length=25)),
                ('desc', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
