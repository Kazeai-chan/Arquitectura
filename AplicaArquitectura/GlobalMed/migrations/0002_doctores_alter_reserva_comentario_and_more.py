# Generated by Django 4.1.2 on 2023-11-12 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GlobalMed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='reserva',
            name='comentario',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]