# Generated by Django 4.0 on 2021-12-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestedWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('phonetic_spelling', models.CharField(max_length=255)),
                ('definition', models.CharField(max_length=255)),
                ('example_sentence', models.CharField(max_length=255)),
                ('bubbe', models.CharField(max_length=255)),
            ],
        ),
    ]
