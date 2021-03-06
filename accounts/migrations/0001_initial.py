# Generated by Django 3.1 on 2022-04-26 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Foto')),
                ('bio', models.TextField(blank=True, verbose_name='Mini bio')),
                ('birthday', models.DateField(blank=True, verbose_name='Nascimento')),
                ('genre', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('cell_phone', models.CharField(blank=True, max_length=14, verbose_name='Celular')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiis',
                'ordering': ['id'],
            },
        ),
    ]
