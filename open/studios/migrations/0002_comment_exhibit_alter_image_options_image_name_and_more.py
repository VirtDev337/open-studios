# Generated by Django 4.0 on 2021-12-09 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('exhibit_id', models.AutoField(primary_key=True, serialize=False)),
                ('exhibit_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('timestamp', models.DateField(auto_now=True)),
                ('featured_date', models.DateField(null=True)),
                ('featured', models.BooleanField(default=False)),
                ('revealed', models.BooleanField(default=False)),
                ('artist_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('website', models.URLField()),
                ('bio', models.TextField()),
                ('comment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='studios.comment')),
            ],
            options={
                'verbose_name_plural': 'Exhibits',
            },
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.CreateModel(
            name='Rotation',
            fields=[
                ('rotation_id', models.AutoField(primary_key=True, serialize=False)),
                ('delay', models.TimeField()),
                ('current', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='exhibit', to='studios.exhibit')),
            ],
            options={
                'verbose_name_plural': 'Roations',
            },
        ),
        migrations.AddField(
            model_name='exhibit',
            name='images',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='exhibit', to='studios.image'),
        ),
        migrations.AddField(
            model_name='exhibit',
            name='tags',
            field=models.ManyToManyField(to='studios.Tag'),
        ),
    ]
