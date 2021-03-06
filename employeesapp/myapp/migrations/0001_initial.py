# Generated by Django 2.2.12 on 2020-05-22 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRST_NAME', models.CharField(max_length=50)),
                ('LAST_NAME', models.CharField(max_length=50)),
                ('EMAIL', models.CharField(max_length=50)),
                ('PHONE_NUMBER', models.CharField(max_length=20)),
                ('HIRE_DATE', models.DateField()),
                ('JOB_ID', models.CharField(max_length=20)),
                ('SALARY', models.IntegerField()),
                ('COMISSION_PCT', models.IntegerField()),
                ('MANAGER_ID', models.CharField(max_length=10)),
                ('DEPARTMENT_ID', models.IntegerField()),
            ],
        ),
    ]
