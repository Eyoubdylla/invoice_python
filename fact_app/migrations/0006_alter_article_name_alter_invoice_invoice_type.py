# Generated by Django 5.1.1 on 2024-10-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fact_app', '0005_alter_invoice_invoice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(choices=[('R', 'RECEIP'), ('P', 'PROFORMA INVOICE'), ('I', 'INVOICE')], max_length=1),
        ),
    ]