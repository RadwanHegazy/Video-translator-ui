from django.db import models



class Application (models.Model) :
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='app/')
    downloads = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'{self.title}'