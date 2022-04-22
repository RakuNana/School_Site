# Generated by Django 3.2.3 on 2022-04-02 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0017_alter_ad_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ad_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ads.ad'),
        ),
    ]