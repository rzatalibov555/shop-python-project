# Generated by Django 4.1.7 on 2023-03-30 16:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaranma tarixi'),
        ),
        migrations.AlterField(
            model_name='category',
            name='uptated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Yenilənmə tarixi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Kateqoriya'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaranma tarixi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıqlama'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_persentage',
            field=models.IntegerField(blank=True, choices=[(5, '5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80'), (85, '85'), (90, '90'), (95, '95'), (100, '100')], null=True, verbose_name='Endirim %'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Endirimli qiymət'),
        ),
        migrations.AlterField(
            model_name='product',
            name='in_sale',
            field=models.BooleanField(default=False, verbose_name='Endirimdə'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Məsulun adı'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Qiymət'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uptated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Yenilənmə tarixi'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaranma tarixi'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='uptated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Yenilənmə tarixi'),
        ),
    ]