# Generated by Django 4.0.4 on 2022-06-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_alter_contract_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
