# Generated by Django 4.1.4 on 2022-12-11 19:16

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('seasons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seasonteamstandings',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
        migrations.AddField(
            model_name='gameteam',
            name='page',
            field=modelcluster.fields.ParentalKey(
                on_delete=django.db.models.deletion.CASCADE, to='seasons.game'
            ),
        ),
        migrations.AddField(
            model_name='gameteam',
            name='team',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.team'
            ),
        ),
    ]