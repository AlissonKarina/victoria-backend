# Generated by Django 3.0.3 on 2020-08-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200805_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='id_answer',
            field=models.ManyToManyField(to='core.AnswerText'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(max_length=500),
        ),
    ]