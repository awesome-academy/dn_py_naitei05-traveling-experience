# Generated by Django 3.2 on 2022-03-22 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_rename_image_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rate_average',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Rate of this post', max_digits=3),
        ),
    ]
