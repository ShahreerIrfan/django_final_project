# Generated by Django 4.2.3 on 2023-09-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_images_product_image_product_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
