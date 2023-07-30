# Generated by Django 4.1.4 on 2023-04-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_deilverytime_order_delivery_day"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="is_delivered",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="وضعیت تحویل"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="delivery_day",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="زمان ارسال"
            ),
        ),
    ]