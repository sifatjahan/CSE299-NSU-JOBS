# Generated by Django 2.1.5 on 2019-03-26 14:29

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
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_email', models.EmailField(max_length=254)),
                ('std_name', models.CharField(max_length=128)),
                ('std_bio', models.CharField(max_length=256, null=True)),
                ('std_contact', models.CharField(max_length=14)),
                ('ssc_int', models.CharField(max_length=256)),
                ('ssc_year', models.CharField(max_length=256)),
                ('ssc_cgpa', models.CharField(max_length=256)),
                ('hsc_int', models.CharField(max_length=256)),
                ('hsc_year', models.CharField(max_length=256)),
                ('hsc_cgpa', models.CharField(max_length=256)),
                ('honor_int', models.CharField(max_length=256)),
                ('honor_year', models.CharField(max_length=256)),
                ('honor_cgpa', models.CharField(max_length=256)),
                ('master_int', models.CharField(max_length=256, null=True)),
                ('master_year', models.CharField(max_length=256, null=True)),
                ('master_cgpa', models.CharField(max_length=256, null=True)),
                ('skills', models.CharField(max_length=2048)),
                ('experience', models.CharField(max_length=2048)),
                ('awards', models.CharField(max_length=2048)),
                ('picture', models.ImageField(upload_to='pp/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
