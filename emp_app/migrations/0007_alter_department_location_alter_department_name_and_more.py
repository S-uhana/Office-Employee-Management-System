# Generated by Django 4.0.2 on 2022-03-06 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0006_alter_employee_dept_alter_employee_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='location',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='bonus',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='emp_app.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='emp_app.role'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
