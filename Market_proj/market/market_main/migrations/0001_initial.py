# Generated by Django 4.1.6 on 2023-02-13 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('password1', models.CharField(max_length=30, verbose_name='Password1')),
                ('password2', models.CharField(max_length=30, verbose_name='Password2')),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='market_main.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_prodct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market_main.product'),
        ),
    ]
