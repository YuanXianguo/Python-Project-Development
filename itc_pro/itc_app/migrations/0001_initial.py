# Generated by Django 2.2.7 on 2019-11-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_pos_id', models.IntegerField()),
                ('sys_time', models.CharField(max_length=20)),
                ('formula', models.CharField(max_length=20)),
                ('test_mode', models.CharField(max_length=20)),
                ('big_leak', models.CharField(blank=True, max_length=20, null=True)),
                ('work_press', models.CharField(blank=True, max_length=20, null=True)),
                ('torque', models.CharField(blank=True, max_length=20, null=True)),
                ('cur_test', models.CharField(blank=True, max_length=20, null=True)),
                ('cur_p1', models.CharField(blank=True, max_length=20, null=True)),
                ('cur_p2', models.CharField(blank=True, max_length=20, null=True)),
                ('error_msg', models.CharField(blank=True, max_length=20, null=True)),
                ('is_pass', models.CharField(blank=True, max_length=5, null=True)),
                ('is_delete', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'test_results',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
