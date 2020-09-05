from django.db import models

# Create your models here.
class College(models.Model):
	name = models.CharField(max_length=60)
	address = models.TextField(max_length=1000)
	class Meta:
		verbose_name = "College"
		verbose_name_plural = "Colleges"
	def __str__(self):
		return str(self.name)
    

class Student(models.Model):
	college = models.ForeignKey(College, on_delete=models.CASCADE, help_text='College')
	name = models.CharField(max_length=50,  help_text='Full Name')
	email = models.EmailField(unique=True, help_text='Email Address')
	message = models.TextField(max_length=1000)
	file = models.FileField()
	class Meta:
		verbose_name = "Student"
		verbose_name_plural = "Student"
	def __str__(self):
		return str(self.email)
    