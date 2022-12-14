# Generated by Django 4.1.1 on 2022-10-09 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_company_collegesuper_co_prn_student_s_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endterm',
            old_name='presentation',
            new_name='present',
        ),
        migrations.AddField(
            model_name='student',
            name='SC',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.company'),
        ),
        migrations.CreateModel(
            name='Cmideterm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_domainandtech', models.IntegerField()),
                ('C_profesethi', models.IntegerField()),
                ('C_interpersonatl', models.IntegerField()),
                ('C_presentation', models.IntegerField()),
                ('C_communication', models.IntegerField()),
                ('C_taskcompleted', models.IntegerField()),
                ('C_questionans', models.IntegerField()),
                ('C_total', models.IntegerField()),
                ('C_SM', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.student')),
            ],
        ),
        migrations.CreateModel(
            name='CEndterm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_background', models.IntegerField()),
                ('C_scopeandobj', models.IntegerField()),
                ('C_implemen', models.IntegerField()),
                ('C_observa', models.IntegerField()),
                ('C_domain', models.IntegerField()),
                ('C_present', models.IntegerField()),
                ('C_communic', models.IntegerField()),
                ('C_interper', models.IntegerField()),
                ('C_profess', models.IntegerField()),
                ('C_qanda', models.IntegerField()),
                ('C_E_total', models.IntegerField()),
                ('C_SE', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.student')),
            ],
        ),
    ]
