# Generated by Django 5.1.4 on 2025-01-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0010_alter_diary_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
