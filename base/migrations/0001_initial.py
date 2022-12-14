# Generated by Django 4.0.6 on 2022-12-02 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('receiver', models.CharField(blank=True, max_length=50, null=True)),
                ('msg_body', models.CharField(blank=True, max_length=1000, null=True)),
                ('msg_subject', models.CharField(blank=True, max_length=20, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
