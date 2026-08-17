from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(null=False,blank=False)
    nickname = models.CharField(max_length=30,null=False,blank=False,unique=True)
    email = models.EmailField(null=False,blank=False,unique=True)
    telefone = models.CharField(null=False,blank=False,unique=True)
    data_nascimento = models.DateField(null=False,blank=False)

    def __str__(self):
        return self.nome