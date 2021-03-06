# Generated by Django 2.0.5 on 2018-05-10 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='建立'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.BooleanField(default=False, verbose_name='完成'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='tag',
            field=models.ManyToManyField(to='todo.Tag', verbose_name='標籤'),
        ),
    ]
