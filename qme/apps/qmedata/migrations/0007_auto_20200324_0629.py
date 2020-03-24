# Generated by Django 3.0.3 on 2020-03-24 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qmedata', '0006_auto_20200322_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='place_equipment',
            field=models.CharField(choices=[('First', 'Первый день'), ('Second', 'Второй день'), ('NoActive', 'Не активна')], max_length=30, verbose_name='Калибровочный день'),
        ),
    ]
