# Generated by Django 2.2.10 on 2020-10-23 06:47

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_councillorgrouppage_members_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='councillorpage',
            name='councillor_groups',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='councillors', to='core.CouncillorGroupPage'),
        ),
    ]
