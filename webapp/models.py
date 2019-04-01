from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    std_email = models.EmailField()
    std_name = models.CharField(max_length=128)
    std_bio = models.CharField(max_length=256, null=True)
    std_contact = models.CharField(max_length=14)
    ssc_int = models.CharField(max_length=256)
    ssc_year = models.CharField(max_length=256)
    ssc_cgpa = models.CharField(max_length=256)
    hsc_int = models.CharField(max_length=256)
    hsc_year = models.CharField(max_length=256)
    hsc_cgpa = models.CharField(max_length=256)
    honor_int = models.CharField(max_length=256)
    honor_year = models.CharField(max_length=256)
    honor_cgpa = models.CharField(max_length=256)
    master_int = models.CharField(max_length=256, null=True)
    master_year = models.CharField(max_length=256, null=True)
    master_cgpa = models.CharField(max_length=256, null=True)
    skills = models.CharField(max_length=2048)
    experience = models.CharField(max_length=2048)
    awards = models.CharField(max_length=2048)
    picture = models.ImageField(upload_to='pp/')

    @receiver(post_save, sender=User)
    def create_student(sender, instance, created, **kwargs):
        if created:
            Student.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_student(sender, instance, **kwargs):
        instance.student.save()

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    com_email = models.EmailField()
    com_name = models.CharField(max_length=128)
    com_bio = models.CharField(max_length=256, null=True)
    com_contact = models.CharField(max_length=14)
    skills = models.CharField(max_length=2048)

    @receiver(post_save, sender=User)
    def create_company(sender, instance, created, **kwargs):
        if created:
            Company.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_company(sender, instance, **kwargs):
        instance.company.save()