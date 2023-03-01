# Generated by Django 4.1.5 on 2023-02-03 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_delete_mashine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'shop_brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'shop_categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('is_new', models.BooleanField(default=False)),
                ('is_discounted', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.brand')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'db_table': 'shop_products',
            },
        ),
    ]