# Generated by Django 4.1.1 on 2022-10-15 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_remove_company_c_email_alter_student_s_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compper',
            name='p_Name',
        ),
    ]
