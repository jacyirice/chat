# Generated by Django 3.1.7 on 2021-05-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20210512_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.ImageField(default='https://static.turbosquid.com/Preview/001292/481/WV/_D.jpg', upload_to='', verbose_name='Imagem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groupuser',
            name='office',
            field=models.SmallIntegerField(choices=[(1, 'Administrador'), (2, 'Membro'), (3, 'Apenas leitura')], default=2),
        ),
        migrations.AlterField(
            model_name='message',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'Entrou no grupo'), (2, 'Saiu do grupo'), (3, 'Mensagem')], default=3),
        ),
    ]
