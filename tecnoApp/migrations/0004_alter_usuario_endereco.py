# Generated by Django 5.1.3 on 2024-12-04 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnoApp', '0003_usuario_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='endereco',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='tecnoApp.endereco'),
        ),
    ]
