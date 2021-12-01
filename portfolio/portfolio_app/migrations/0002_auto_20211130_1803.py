# Generated by Django 3.2.9 on 2021-11-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='resume',
            name='resume_file',
            field=models.FileField(upload_to='static/uploads/'),
        ),
    ]