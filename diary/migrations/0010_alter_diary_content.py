# Generated by Django 5.1.4 on 2025-01-27 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0009_alter_comment_created_at_alter_diary_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
