# Generated by Django 2.0.4 on 2018-04-14 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_complaint_light_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Lt_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Lights'),
        ),
    ]