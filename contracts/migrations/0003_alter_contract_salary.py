from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_alter_contract_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='salary',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
