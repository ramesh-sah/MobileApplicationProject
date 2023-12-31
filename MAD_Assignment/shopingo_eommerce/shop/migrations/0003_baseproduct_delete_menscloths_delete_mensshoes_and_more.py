# Generated by Django 4.2.4 on 2023-12-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_menscloths_mensshoes_menswatches_womensglasses_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='products')),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='MensCloths',
        ),
        migrations.DeleteModel(
            name='MensShoes',
        ),
        migrations.DeleteModel(
            name='MensWatches',
        ),
        migrations.DeleteModel(
            name='WomensGlasses',
        ),
        migrations.DeleteModel(
            name='WomensHandbags',
        ),
    ]