# Generated by Django 3.0.3 on 2020-08-05 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200805_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_question',
            field=models.ManyToManyField(to='core.AnswerText'),
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='parameter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Parameter'),
        ),
    ]