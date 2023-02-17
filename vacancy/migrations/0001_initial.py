# Generated by Django 4.1.6 on 2023-02-17 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('titel', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('titel', models.CharField(max_length=12)),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False, unique=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='game.game')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('US', 'United States'), ('RU', 'Russia'), ('KG', 'Kyrgyzstan'), ('KZ', 'Kazakhastan')], max_length=30)),
                ('demands', models.TextField()),
                ('privileges', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy', to='vacancy.team')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy', to='vacancy.role')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy', to='game.game')),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='vacancy.team'),
        ),
    ]
