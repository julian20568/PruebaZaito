# Generated by Django 3.2.9 on 2021-11-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('price', models.IntegerField()),
                ('paused', models.BooleanField()),
            ],
        ),
    ]
