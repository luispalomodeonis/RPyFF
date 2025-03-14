# Generated by Django 5.1.4 on 2025-01-12 18:07

import datetime
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Letra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('letra', models.CharField(max_length=1, unique=True, verbose_name='Letra')),
            ],
            options={
                'ordering': ['letra'],
            },
        ),
        migrations.CreateModel(
            name='Origen',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(help_text='Introduce un nombre de Origen', max_length=120, verbose_name='Nombre')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Registrado')),
                ('estado', models.CharField(blank=True, choices=[('r', 'Revisión'), ('a', 'Aprobado')], default='r', max_length=1, verbose_name='Estado')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Palabra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('palabra', models.CharField(help_text='Introduce una palabra', max_length=51, verbose_name='Palabra')),
                ('significado', models.TextField(default='', help_text='Introduce el significado de la palabra', max_length=512, verbose_name='Significado')),
                ('fecha', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Registrada')),
                ('estado', models.CharField(blank=True, choices=[('r', 'Revisión'), ('a', 'Aprobada')], default='r', max_length=1, verbose_name='Estado')),
                ('creador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('letra', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='rpyff.letra')),
                ('origen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='rpyff.origen')),
            ],
            options={
                'ordering': ['palabra', 'letra', 'origen', 'fecha'],
            },
        ),
        migrations.CreateModel(
            name='Refran',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('dicho', models.TextField(help_text='Introduce el refrán', max_length=191, verbose_name='Refrán')),
                ('explicacion', models.TextField(help_text='Introduce una explicación para el refrán', max_length=512, verbose_name='Explicación')),
                ('fecha', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Registrado')),
                ('fechaaprobacion', models.DateField(blank=True, null=True, verbose_name='Aprobado')),
                ('fechapublicacion', models.DateField(blank=True, null=True, verbose_name='Publicado')),
                ('estado', models.CharField(blank=True, choices=[('r', 'Revisión'), ('a', 'Aprobado'), ('p', 'Publicado')], default='r', max_length=1, verbose_name='Estado')),
                ('creador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('letra', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='rpyff.letra')),
                ('origen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='rpyff.origen')),
                ('otraspalabras', models.ManyToManyField(to='rpyff.palabra')),
                ('palabra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='palabra_base', to='rpyff.palabra')),
            ],
            options={
                'ordering': ['palabra', 'fecha', 'fechaaprobacion', 'fechapublicacion'],
            },
        ),
    ]
