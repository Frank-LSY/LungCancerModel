# Generated by Django 4.2.1 on 2023-08-29 03:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0009_alter_detail_choice_alter_probability_probability"),
    ]

    operations = [
        migrations.AddField(
            model_name="detail",
            name="probability",
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
