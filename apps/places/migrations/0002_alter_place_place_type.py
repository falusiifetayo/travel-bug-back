# Generated by Django 4.1.3 on 2022-11-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_type',
            field=models.CharField(choices=[('1', 'Private and Luxury'), ('Full-day Tours', 'Full-day Tours'), ('Day trips', 'Day trips'), ('Forest', 'Forest'), ('Favourites', 'Favourites')], max_length=50, verbose_name='Place Type'),
        ),
    ]
