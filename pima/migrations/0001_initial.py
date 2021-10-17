# Generated by Django 3.2.8 on 2021-10-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('pregnancies', models.IntegerField()),
                ('glucose', models.FloatField()),
                ('bloodpressure', models.FloatField()),
                ('skinthickness', models.FloatField()),
                ('insulin', models.FloatField()),
                ('bmi', models.FloatField()),
                ('diabetespedigree', models.FloatField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
