# Generated by Django 5.0.2 on 2024-02-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0016_taskmonsaraf_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
