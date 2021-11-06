from django.db import models

# Create your models here.


class Private(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    email      = models.EmailField()
    DOF        = models.DateField()
    age        = models.IntegerField()

    def __str__(self):

        return '{} {} {}'.format(self.first_name,'-',self.age)




class Public(models.Model):
      url  = models.URLField()
      name = models.CharField(max_length=20)

      def __str__(self):
          return '{} {} {}'.format(self.url, '-', self.name)

