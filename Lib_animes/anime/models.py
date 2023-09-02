from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=100)
    
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nome

class Anime(models.Model):
    anime = models.CharField(max_length=100)

    descrição = models.TextField(max_length=500)

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    completo = models.BooleanField(default=False)






