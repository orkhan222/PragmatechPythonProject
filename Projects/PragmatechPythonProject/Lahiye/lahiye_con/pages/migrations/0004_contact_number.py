# Generated by Django 3.2.3 on 2021-07-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210715_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]