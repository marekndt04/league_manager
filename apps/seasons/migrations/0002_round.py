# Generated by Django 4.0.4 on 2022-05-22 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('seasons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                (
                    'page_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='wagtailcore.page',
                    ),
                ),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]