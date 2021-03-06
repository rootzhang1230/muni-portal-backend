# Generated by Django 2.2.10 on 2020-10-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201010_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetail',
            name='purpose',
            field=models.CharField(default='', help_text='Internal reminder of what this represents - e.g. "Office number for Joanne Smith"', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='annotation',
            field=models.CharField(blank=True, help_text='Optional public note of what this contact is for, e.g. "Senior Library Assistant Ms E. October" or "Videlia AugustCell phone number"', max_length=250, null=True),
        ),
    ]
