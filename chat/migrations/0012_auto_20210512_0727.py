# Generated by Django 3.1.7 on 2021-05-12 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_auto_20210512_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupuser',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='chat.group', verbose_name='group'),
        ),
        migrations.AlterField(
            model_name='groupuser',
            name='office',
            field=models.SmallIntegerField(choices=[(2, 'Membro'), (1, 'Administrador'), (3, 'Apenas leitura')], default=2),
        ),
        migrations.AlterField(
            model_name='message',
            name='type',
            field=models.SmallIntegerField(choices=[(2, 'Saiu do grupo'), (1, 'Entrou no grupo'), (3, 'Mensagem')], default=3),
        ),
    ]
