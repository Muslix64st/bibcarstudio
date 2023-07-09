# Generated by Django 4.2.2 on 2023-06-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiBcar', '0002_alter_content_photo_b_alter_content_photo_l_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('car_number', models.CharField(max_length=8, verbose_name='Номер машины')),
                ('message', models.CharField(max_length=500, verbose_name='Задайте вопрос или уточните время в какое вам перезвонить')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
            ],
            options={
                'verbose_name': 'Клиенты',
                'verbose_name_plural': 'клиенты',
                'ordering': ['phone_number', 'car_number'],
            },
        ),
        migrations.AlterField(
            model_name='categorycontent',
            name='name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Категория'),
        ),
    ]