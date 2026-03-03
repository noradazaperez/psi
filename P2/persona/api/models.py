from django.db import models

class Persona(models.Model):
    """Model representing a person."""
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        """String for representing the Model object."""
        return self.nombre + ' ' + self.apellido

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        # return reverse('book-detail', args=[str(self.id)])
        pass

    class Meta:
        ordering = ['id']
