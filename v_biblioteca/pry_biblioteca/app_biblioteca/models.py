from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.name + ' ' + self.surname

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    route = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
    
    def __str__(self):
        return self.title
