# Generated by Django 4.2.1 on 2023-05-24 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.curso')),
            ],
        ),
    ]
