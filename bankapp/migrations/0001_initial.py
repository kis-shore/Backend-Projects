# Generated by Django 4.2.2 on 2023-06-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=11)),
                ('bank_id', models.IntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=20)),
            ],
        ),
    ]