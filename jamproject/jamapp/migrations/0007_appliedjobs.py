# Generated by Django 4.0 on 2022-09-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamapp', '0006_jobs_emailaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empemailaddress', models.EmailField(max_length=50)),
                ('jobtitle', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.EmailField(max_length=50)),
                ('dob', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=20)),
                ('keyskills', models.TextField()),
                ('applieddate', models.CharField(max_length=30)),
            ],
        ),
    ]
