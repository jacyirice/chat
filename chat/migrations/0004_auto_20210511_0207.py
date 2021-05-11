# Generated by Django 3.1.7 on 2021-05-11 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_auto_20210511_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'Entrou no grupo'), (3, 'Mensagem'), (2, 'Saiu do grupo')], default=3),
        ),
        migrations.AlterField(
            model_name='groupuser',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.group', verbose_name='group'),
        ),
        migrations.AlterField(
            model_name='groupuser',
            name='office',
            field=models.SmallIntegerField(choices=[(3, 'Apenas leitura'), (1, 'Administrador'), (2, 'Membro')], default=2),
        ),
        migrations.AlterField(
            model_name='groupuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_groups', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='message',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.group'),
        ),
    ]
