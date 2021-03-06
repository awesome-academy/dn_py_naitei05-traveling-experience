# Generated by Django 3.2 on 2022-03-12 14:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.profile'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='followed_id',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.PROTECT, related_name='followed', to='post.profile'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='follower_id',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.PROTECT, related_name='follower', to='post.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.profile'),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.post'),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.tag'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.post'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.profile'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='content',
            field=models.CharField(help_text='Enter content for this tag', max_length=200),
        ),
    ]
