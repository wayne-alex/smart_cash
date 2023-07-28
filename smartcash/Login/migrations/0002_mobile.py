# Generated by Django 4.2.3 on 2023-07-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]