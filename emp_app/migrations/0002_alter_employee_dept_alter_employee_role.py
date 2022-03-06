# Generated by Django 4.0.2 on 2022-03-05 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='emp_app.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey( default=None ,on_delete=django.db.models.deletion.CASCADE, to='emp_app.role'),
        ),
    ]