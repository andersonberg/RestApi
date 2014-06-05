from django.db import models

class Alternativa(models.Model):
    url = models.URLField()
    peso = models.IntegerField()

class RestApi(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    alternativas = models.ManyToManyField(Alternativa)

    def __str__(self):
        return self.name

