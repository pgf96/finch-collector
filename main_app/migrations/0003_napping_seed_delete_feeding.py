# Generated by Django 4.1.5 on 2023-01-19 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Napping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='nap date')),
                ('nap', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('E', 'Evening')], default='M', max_length=1)),
                ('finch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.finch')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Feeding',
        ),
    ]
