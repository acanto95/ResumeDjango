from django.db import models

class MainInfo(models.Model):
    
    name = models.CharField(max_length=255, blank=False, unique=True)
    birthday = models.CharField(max_length=255, blank=False, unique=True)
    adress = models.CharField(max_length=255, blank=False, unique=True)
    phonenum = models.CharField(max_length=255, blank=False, unique=True)

    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class ExperienceInfo(models.Model):
    company = models.CharField(max_length=255, blank=False)
    position = models.CharField(max_length=255, blank=False)
    dates = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255,blank=False)

    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class SkillsInfo(models.Model):
    
    technology = models.CharField(max_length=255, blank=False)
    timeskill = models.CharField(max_length=100)

    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class ProyectsInfo(models.Model):
    
    proyectname = models.CharField(max_length=255, blank=False)
    positionproy = models.CharField(max_length=255, blank=False)
    descriptionproy = models.CharField(max_length=255, blank=False)
    techinvolved = models.CharField(max_length=255, blank=False)


    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Comments(models.Model):
    
    commentname = models.CharField(max_length=255, blank=False)
    comment = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)




