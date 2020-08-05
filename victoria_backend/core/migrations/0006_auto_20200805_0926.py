# Generated by Django 3.0.3 on 2020-08-05 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200805_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answertext',
            old_name='id_paper',
            new_name='paper',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='id_parameter',
            new_name='parameter',
        ),
        migrations.RemoveField(
            model_name='question',
            name='id_answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.ManyToManyField(to='core.AnswerText'),
        ),
    ]