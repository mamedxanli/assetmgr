# Generated by Django 2.0.6 on 2018-09-28 14:30

from django.db import migrations, models
import django.db.models.deletion
import netdev.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Netdev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(default=None, max_length=100)),
                ('hostname', models.CharField(default=None, max_length=100, verbose_name='Hostname')),
                ('decomissioned', models.BooleanField(default=False, verbose_name='Decomissioned')),
                ('decomissioned_date', models.DateField(default='2023-12-31')),
                ('location', models.CharField(default=None, max_length=100, verbose_name='Location')),
                ('device_type', models.CharField(max_length=30, verbose_name='Device type')),
                ('brand', models.CharField(max_length=20, verbose_name='Brand')),
                ('netdev_model', models.CharField(max_length=20, verbose_name='Model')),
                ('generation', models.CharField(max_length=5, verbose_name='Generation')),
                ('manufacture_year', models.IntegerField(verbose_name='Year of manufacture')),
                ('os', models.CharField(default=None, max_length=100, verbose_name='Device image')),
                ('port_number', models.IntegerField(verbose_name='Number of physical network ports')),
                ('port_description', models.CharField(max_length=50, verbose_name='Port description')),
                ('serial_number', models.CharField(max_length=20, verbose_name='Serial number')),
                ('company_asset_number', models.CharField(max_length=30, verbose_name='Company Asset Number')),
                ('warranty', models.CharField(max_length=100, verbose_name='Warranty status')),
                ('current_roles', models.CharField(max_length=100, verbose_name='Current roles')),
                ('ip_v4_address', models.CharField(default=None, max_length=100, verbose_name='Private ipv4 address')),
                ('ip_v4_address_public', models.CharField(default=None, max_length=100, verbose_name='Public ipv4 address')),
                ('ip_v6_address', models.CharField(default=None, max_length=100, verbose_name='IPv6 address')),
                ('file_picture_1', models.FileField(blank=True, default=None, upload_to=netdev.models.save_directory_path, verbose_name='Front Picture')),
                ('file_picture_2', models.FileField(blank=True, default=None, upload_to=netdev.models.save_directory_path, verbose_name='Back Picture')),
                ('file_other', models.FileField(blank=True, default=None, upload_to=netdev.models.save_directory_path, verbose_name='Other file/Zip file if many')),
                ('other', models.TextField(max_length=500, verbose_name='Notes')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
            options={
                'verbose_name_plural': 'Network Devices',
            },
        ),
    ]
