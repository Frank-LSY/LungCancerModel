# Generated by Django 4.2.1 on 2023-05-18 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0005_alter_detail_pollid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="detail",
            name="pollid",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="poll",
                to="polls.history",
            ),
        ),
    ]
