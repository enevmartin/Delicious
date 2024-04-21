# Generated by Django 5.0.3 on 2024-04-20 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_remove_recipe_categories_recipe_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('1', 'Recipe Categories'), ('2', 'Breakfast'), ('3', 'Lunch'), ('4', 'Dinner'), ('5', 'Appetizers')], default='1', max_length=100),
        ),
    ]
