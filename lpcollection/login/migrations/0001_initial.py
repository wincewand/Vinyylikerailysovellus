# Generated by Django 2.2.10 on 2020-03-30 13:25

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
    ]
