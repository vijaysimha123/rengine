# Generated by Django 3.1.3 on 2021-03-07 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0002_enginetype_interesting_subdomain_lookup'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestingLookupModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='enginetype',
            name='interesting_subdomain_lookup',
        ),
    ]