# Generated by Django 3.0.6 on 2020-06-01 06:32

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
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['last_modified'],
            },
        ),
        migrations.CreateModel(
            name='ChoiceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_group', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-last_modified'],
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=2)),
                ('display_order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['subject'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name='Question')),
                ('notes', models.TextField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('review_status', models.CharField(blank=True, choices=[('UR', 'Unreviewed'), ('PN', 'Pending'), ('AP', 'Approved')], default='UR', max_length=100, null=True, verbose_name='Review Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questions.Choice', verbose_name='Correct Answer')),
                ('choice_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questions.ChoiceGroup', verbose_name='Choice Group')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('level', models.ManyToManyField(to='questions.Level')),
                ('subject', models.ManyToManyField(to='questions.Subject')),
            ],
            options={
                'ordering': ['-last_modified'],
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questions.ChoiceGroup'),
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together={('choice', 'choice_group')},
        ),
    ]
