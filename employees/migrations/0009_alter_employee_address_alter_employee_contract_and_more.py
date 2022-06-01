# Generated by Django 4.0.4 on 2022-06-01 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_alter_address_postal_code'),
        ('contracts', '0004_alter_contract_work_shift'),
        ('personal_documents', '0003_alter_personal_document_cnpj_and_more'),
        ('employees', '0008_alter_employee_personal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='addresses.address'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='contract',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contracts.contract'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='personal_documents',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personal_documents.personal_document'),
        ),
    ]