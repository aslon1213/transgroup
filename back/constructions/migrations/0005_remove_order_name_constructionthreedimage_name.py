# Generated by Django 5.0 on 2023-12-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0004_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='constructionthreedimage',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]