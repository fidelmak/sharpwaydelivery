# Generated by Django 4.0.5 on 2022-07-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='posts')),
                ('text', models.TextField(max_length=400)),
            ],
        ),
    ]
