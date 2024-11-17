from django.db import models

    
class Client_update(models.Model):
    firstname = models.CharField(blank=False , max_length=20)
    lastname = models.CharField(blank=False , max_length=20)
    about = models.TextField(blank=False)
    exp_years = models.CharField(blank=True , max_length=20)
    photo = models.ImageField(blank=True, upload_to="images/")
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=255, null=False, default="Unknown")  # Default value here
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}\t{}".format(self.firstname , self.lastname)