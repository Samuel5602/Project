# Generated by Django 3.1.3 on 2020-11-14 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biertrofee', '0004_auto_20201113_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='poule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='match_poule', to='biertrofee.poul'),
        ),
    ]
