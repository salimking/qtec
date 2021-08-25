# Generated by Django 3.2.5 on 2021-08-24 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ('-title',), 'verbose_name': 'Search Menu'},
        ),
        migrations.CreateModel(
            name='keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.story')),
            ],
        ),
    ]