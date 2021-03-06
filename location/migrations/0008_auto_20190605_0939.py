# Generated by Django 2.1.8 on 2019-06-05 09:39

import django.contrib.postgres.fields
import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_auto_20190425_1440'),
    ]

    operations = [
        migrations.RunSQL("DROP INDEX IF EXISTS location_si_workflo_768d25_gin"),
        migrations.AlterField(
            model_name='siteprofile',
            name='workflowlevel2_uuid',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=36), blank=True, help_text='Array of WorkflowLevel2s associated with the SiteProfile.', null=True, size=None),
        ),
        migrations.AddIndex(
            model_name='siteprofile',
            index=django.contrib.postgres.indexes.GinIndex(fields=['workflowlevel2_uuid'], name='location_si_workflo_768d25_gin'),
        ),
    ]
