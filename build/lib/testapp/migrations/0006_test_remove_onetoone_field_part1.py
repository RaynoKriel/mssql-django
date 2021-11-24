# Generated by Django 3.0.4 on 2020-04-20 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_test_issue45_unique_type_change_part2'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRemoveOneToOneFieldModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=50)),
                ('b', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testapp.TestRemoveOneToOneFieldModel')),
            ],
        ),
    ]
