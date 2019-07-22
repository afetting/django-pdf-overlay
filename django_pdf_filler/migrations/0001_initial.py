# Generated by Django 2.2.3 on 2019-07-12 22:07

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django_pdf_filler.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='F:\\Projects\\django_pdf\\media\\forms\\documents'), upload_to='', validators=[django_pdf_filler.validators.validate_pdf])),
                ('times_used', models.PositiveIntegerField(default=0)),
                ('inserted', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=0)),
                ('image', models.FileField(blank=True, null=True, upload_to='django_pdf_filler/layouts/')),
                ('width', models.PositiveIntegerField(default=612)),
                ('height', models.PositiveIntegerField(default=792)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='django_pdf_filler.Document')),
            ],
            options={
                'ordering': ['number'],
                'unique_together': {('document', 'number')},
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('x', models.IntegerField(default=10)),
                ('y', models.IntegerField(default=10)),
                ('default', models.CharField(blank=True, max_length=255)),
                ('system_info', models.CharField(blank=True, max_length=255)),
                ('obj_name', models.CharField(blank=True, max_length=255)),
                ('font_size', models.IntegerField(default=12)),
                ('font_color', models.CharField(default='black', max_length=50)),
                ('font', models.CharField(default='Helvetica', max_length=50)),
                ('inserted', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='django_pdf_filler.Page')),
            ],
        ),
    ]
