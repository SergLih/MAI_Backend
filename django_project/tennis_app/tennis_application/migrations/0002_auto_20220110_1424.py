# Generated by Django 3.0 on 2022-01-10 14:24
import os
from django.db import migrations, models

#def move_m1(apps, schema_editor):
#    LogEntry = apps.get('admin.logentry')

class Migration(migrations.Migration):

    dependencies = [
        ('tennis_application', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_DB_NAME = os.getenv('POSTGRES_DB')
        DJANGO_SU_NAME = os.getenv('POSTGRES_USER')
        # DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
        DJANGO_SU_PASSWORD = os.getenv('POSTGRES_PASSWORD')

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            # email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)

        superuser.save()

    operations = [
        #migrations.RunPython(move_m1),
        migrations.RunPython(generate_superuser),
        migrations.AlterField(
            model_name='player',
            name='birthday',
            field=models.DateTimeField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='player',
            name='count_wons',
            field=models.PositiveIntegerField(verbose_name='Количество побед'),
        ),
        migrations.AlterField(
            model_name='player',
            name='family',
            field=models.CharField(max_length=30, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=15, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='player',
            name='sex',
            field=models.IntegerField(blank=True, choices=[(0, 'Мужчина'), (1, 'Женщина')], null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название организации'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='sponsor_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='begin_tur',
            field=models.DateTimeField(verbose_name='Начало'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='category',
            field=models.IntegerField(blank=True, choices=[(0, 'I'), (1, 'II'), (2, 'III'), (3, 'IV')], null=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='end_tur',
            field=models.DateTimeField(verbose_name='Окончание'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название турнира'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tournament_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
