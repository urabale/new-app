# Generated by Django 3.2.9 on 2021-11-08 15:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zerowaste', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_address',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='住所'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='投稿日時'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(upload_to='media/', verbose_name='写真'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_price',
            field=models.PositiveIntegerField(verbose_name='値段'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=200, verbose_name='商品名'),
        ),
    ]
