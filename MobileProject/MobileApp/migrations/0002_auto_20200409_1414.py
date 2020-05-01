# Generated by Django 3.0.5 on 2020-04-09 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MobileApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colorname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField()),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('ram', models.CharField(max_length=100)),
                ('frontcam', models.CharField(max_length=100)),
                ('rearcam', models.CharField(max_length=200)),
                ('product_code', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MobileApp.brand')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('mobilenum', models.IntegerField()),
                ('emailid', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('isActive', models.BooleanField()),
            ],
        ),
        migrations.RenameField(
            model_name='category',
            old_name='categoryname',
            new_name='category_name',
        ),
        migrations.DeleteModel(
            name='Mobile',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MobileApp.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MobileApp.color'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MobileApp.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MobileApp.users'),
        ),
    ]