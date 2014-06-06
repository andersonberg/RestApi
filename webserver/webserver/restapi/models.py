from django.db import models
from django.utils.text import slugify

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

    #muda o padrão do slug na hora de salvar
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.replace(" ","_"))[:50]
            return super(RestApi, self).save(*args, **kwargs)
