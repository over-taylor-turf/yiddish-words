# Generated by Django 4.0 on 2021-12-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_suggestedword'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestedword',
            name='email',
            field=models.CharField(default='stackoverturf@gmail.com', max_length=255),
            preserve_default=False,
        ),
    ]
