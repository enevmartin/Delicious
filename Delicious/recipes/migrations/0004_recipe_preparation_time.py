# Generated by Django 5.0.3 on 2024-04-19 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='preparation_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]