# Generated by Django 3.2.12 on 2022-10-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_teams_name3'),
    ]

    operations = [
        migrations.CreateModel(
            name='crossOpen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeamName', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('Name_of_Poc', models.CharField(max_length=100)),
                ('contactno', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=40, null=True)),
                ('info', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='adjudicators',
            name='email',
            field=models.EmailField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='adjudicators',
            name='info',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
