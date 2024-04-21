# Generated by Django 5.0.3 on 2024-04-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('BBQ', 'BBQ'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Appetizers', 'Appetizers')], default='1', max_length=100),
        ),
    ]
