# Generated by Django 3.0.6 on 2020-05-19 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('adr', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('order_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='paymentCP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=300)),
                ('order_id', models.CharField(max_length=100)),
                ('signature_hash', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arc.DonationUser')),
            ],
        ),
    ]
