# Generated by Django 4.0.2 on 2022-03-05 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_alter_employee_dept_alter_employee_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='emp_app.role'),
        ),
    ]
