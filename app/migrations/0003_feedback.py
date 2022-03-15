# Generated by Django 4.0.2 on 2022-03-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_feedback_delete_ipbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='NA', max_length=30)),
                ('Email', models.CharField(default='NA', max_length=50)),
                ('Query', models.CharField(default='NA', max_length=500)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]