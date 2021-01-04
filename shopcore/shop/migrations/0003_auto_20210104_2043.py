# Generated by Django 3.1.1 on 2021-01-04 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201128_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Купон')),
                ('amount', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Скидочный купон',
                'verbose_name_plural': 'Скидочные купоны',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='placeholder.png', upload_to='image_product/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.coupondiscount', verbose_name='Скидочный купон'),
        ),
    ]