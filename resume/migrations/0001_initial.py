# Generated by Django 4.1.4 on 2023-02-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('git_hub', models.URLField()),
                ('description', models.TextField()),
                ('resume', models.FileField(upload_to='vacancy_resume/')),
                ('about_us', models.TextField(choices=[('from media', 'from media'), ('from sanfransico', 'sarafannor radio'), ('my answer', 'other')])),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
            },
        ),
    ]
