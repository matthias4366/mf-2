# Generated by Django 2.2.1 on 2019-06-10 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RawIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('where_to_buy', models.CharField(blank=True, max_length=100, null=True)),
                ('source_nutritional_information', models.CharField(blank=True, max_length=100, null=True)),
                ('calories', models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True)),
                ('carbohydrates', models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True)),
                ('magnesium', models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True)),
                ('reference_amount', models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True)),
                ('amount_in_package', models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]