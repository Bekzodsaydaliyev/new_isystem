# Generated by Django 4.1.4 on 2022-12-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_index=True, max_length=222),
        ),
    ]
