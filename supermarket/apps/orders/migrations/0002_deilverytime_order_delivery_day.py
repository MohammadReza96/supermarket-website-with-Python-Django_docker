# Generated by Django 4.1.4 on 2023-04-08 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeilveryTime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "delivery_day",
                    models.CharField(max_length=50, verbose_name="زمان ارسال"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="وضعیت روز"),
                ),
            ],
            options={
                "verbose_name": "زمان ارسال",
                "verbose_name_plural": "زمان ارسال",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="delivery_day",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="orders.deilverytime",
                verbose_name="زمان ارسال",
            ),
        ),
    ]
