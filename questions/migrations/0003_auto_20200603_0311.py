# Generated by Django 3.0.6 on 2020-06-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200601_0427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-last_modified']},
        ),
        migrations.AlterField(
            model_name='question',
            name='review_status',
            field=models.CharField(blank=True, choices=[('UNREVIEWED', 'UNREVIEWED'), ('PENDING', 'PENDING'), ('REJECTED', 'REJECTED'), ('ACCEPTED', 'ACCEPTED'), ('FINALIZED', 'FINALIZED')], default='UNREVIEWED', max_length=100, null=True, verbose_name='Review Status'),
        ),
    ]
