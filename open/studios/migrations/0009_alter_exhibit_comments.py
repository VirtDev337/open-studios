# Generated by Django 4.0 on 2021-12-11 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0008_alter_exhibit_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='comments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='exhibit', to='studios.comment'),
        ),
    ]
