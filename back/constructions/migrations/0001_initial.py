# Generated by Django 5.0 on 2023-12-19 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='constructions/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateTimeField(auto_now_add=True)),
                ('to_date', models.DateTimeField(auto_now_add=True)),
                ('construction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructions.construction')),
            ],
        ),
    ]
