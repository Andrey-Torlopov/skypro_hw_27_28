# Generated by Django 4.1.7 on 2023-03-03 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ad",
            options={"verbose_name": "Объявление", "verbose_name_plural": "Объявления"},
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
        migrations.RemoveField(
            model_name="ad",
            name="address",
        ),
        migrations.AddField(
            model_name="ad",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ads.category",
            ),
        ),
        migrations.AddField(
            model_name="ad",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="ad_img/"),
        ),
    ]
