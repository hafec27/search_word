# Generated by Django 5.0.6 on 2025-01-27 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_post_product_image_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('miracle', '奇跡'), ('amazement', '驚嘆'), ('thought', '思索'), ('fantasy', '幻想'), ('strange', '奇妙'), ('other', 'その他')], max_length=50),
        ),
    ]
