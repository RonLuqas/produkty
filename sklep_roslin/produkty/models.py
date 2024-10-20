from django.db import models

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

class Tag(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    tagi = models.ManyToManyField(Tag)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    opis = models.TextField()
    sadzonka_image = models.ImageField(upload_to='images/')
    mlode_drzewo_image = models.ImageField(upload_to='images/')
    dorosle_drzewo_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nazwa

class Dostawa(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    typ = models.CharField(max_length=100, choices=[('mała', 'Mała'), ('duża', 'Duża')])
    koszt = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.typ} - {self.koszt} PLN"


