# Generated by Django 3.1.7 on 2021-02-26 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location', models.CharField(max_length=30)),
                ('location_id', models.CharField(default=0, max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='products/')),
                ('product_id', models.CharField(default=0, max_length=20, primary_key=True, serialize=False)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.location')),
            ],
        ),
    ]