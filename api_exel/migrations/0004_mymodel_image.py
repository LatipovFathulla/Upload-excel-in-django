# Generated by Django 4.1.7 on 2023-03-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_exel', '0003_rename_title_mymodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='image',
            field=models.FileField(null=True, upload_to='img'),
        ),
    ]
