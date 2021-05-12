from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()
# Create your models here.


class Group(models.Model):
    image = models.ImageField(_("Imagem"), upload_to='group/')
    title = models.CharField(_("Titulo do grupo"), max_length=50)
    description = models.CharField(_("Descrição"), max_length=255)
    limit = models.PositiveIntegerField(_("Limite de pessoas por grupo"))

    def __str__(self):
        return f'{self.title}'


class GroupUser(models.Model):
    OFFICE_CHOICE = {
        (1, 'Administrador'),
        (2, 'Membro'),
        (3, 'Apenas leitura')
    }
    office = models.SmallIntegerField(choices=OFFICE_CHOICE, default=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_(
        "user"), related_name="my_groups")
    group = models.ForeignKey("chat.Group", verbose_name=_(
        "group"), on_delete=models.CASCADE, related_name="members")


class Message(models.Model):
    TYPE_CHOICE = {
        (1, 'Entrou no grupo'),
        (2, 'Saiu do grupo'),
        (3, 'Mensagem')
    }
    date_time = models.DateTimeField(_(""), auto_now=True, auto_now_add=False)
    content = models.TextField(_("Conteudo da mensagem"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(
        "chat.Group", related_name="messages", on_delete=models.CASCADE)
    type = models.SmallIntegerField(choices=TYPE_CHOICE, default=3)

    def __str__(self):
        return f'{self.content}'

    class Meta:
        ordering = ['date_time']
