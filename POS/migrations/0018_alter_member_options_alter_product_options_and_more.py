# Generated by Django 5.0.2 on 2024-02-19 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0017_alter_member_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'العضو', 'verbose_name_plural': 'الاعضاء'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'المنتج', 'verbose_name_plural': 'المنتجات'},
        ),
        migrations.AlterModelOptions(
            name='productmetadata',
            options={'verbose_name': 'اسم المنتج', 'verbose_name_plural': 'اسماء المنتجات'},
        ),
        migrations.AlterModelOptions(
            name='tarfehmonsaraf',
            options={'verbose_name': 'منصرف الترفيه', 'verbose_name_plural': 'منصرفات الترفيه'},
        ),
        migrations.AlterModelOptions(
            name='taskmonsaraf',
            options={'verbose_name': 'منصرف الجاف', 'verbose_name_plural': 'منصرفات الجاف'},
        ),
        migrations.AlterModelOptions(
            name='taskmortgaa',
            options={'verbose_name': 'مرتجع الجاف', 'verbose_name_plural': 'مرتجعات الجاف'},
        ),
        migrations.AlterModelOptions(
            name='tazamonsaraf',
            options={'verbose_name': 'منصرف الطازة', 'verbose_name_plural': 'منصرفات الطازة'},
        ),
        migrations.AlterModelOptions(
            name='tazatayyen',
            options={'verbose_name': 'مقررات التعينات', 'verbose_name_plural': 'مقررات التعينات'},
        ),
    ]
