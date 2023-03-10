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
                ('email', models.EmailField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('git_hub', models.URLField()),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('country', models.CharField(choices=[('US', 'United States'), ('RU', 'Russia'), ('KG', 'Kyrgyzstan'), ('KZ', 'Kazakhastan')], max_length=30)),
                ('resume', models.FileField(upload_to='vacancy_resume/')),
                ('about_us', models.CharField(choices=[('from media', 'from media'), ('from sanfransico', 'sarafannor radio'), ('other', 'my answer')], max_length=20)),
                ('my_answer_for_about_us', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
            },
        ),
    ]
