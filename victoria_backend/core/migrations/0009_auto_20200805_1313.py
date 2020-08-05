# Generated by Django 3.0.3 on 2020-08-05 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200805_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer_question',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_text',
            field=models.ManyToManyField(related_name='answer_texts', to='core.AnswerText'),
        ),
        migrations.AlterField(
            model_name='question',
            name='parameter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='core.Parameter'),
        ),
    ]
