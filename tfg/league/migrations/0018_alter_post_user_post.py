# Generated by Django 4.1.5 on 2023-06-08 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0017_remove_post_runes1_remove_post_runes2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.user'),
        ),
    ]
