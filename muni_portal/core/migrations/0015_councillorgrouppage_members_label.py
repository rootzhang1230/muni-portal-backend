# Generated by Django 2.2.10 on 2020-10-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20201022_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='councillorgrouppage',
            name='members_label',
            field=models.CharField(default='Members of this group are', max_length=100),
        ),
    ]
