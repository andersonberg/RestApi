from django.db import models
from django.utils.text import slugify


class Alternativa(models.Model):
    url = models.URLField()
    peso = models.IntegerField()
    sorteios = models.IntegerField(null=True)


class User(models.Model):
    username = models.CharField(max_length=30)
    alternativa = models.OneToOneField(Alternativa, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.username

    #muda o padrão do slug na hora de salvar
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username.replace(" ", "_"))[:50]
        return super(User, self).save(*args, **kwargs)


class Experimento(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    alternativas = models.ManyToManyField(Alternativa)
    #users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    #muda o padrão do slug na hora de salvar
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.replace(" ", "_"))[:50]
        return super(Experimento, self).save(*args, **kwargs)
