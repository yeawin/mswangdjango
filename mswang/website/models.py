from django.db import models

# Create your models here.
class Subject(models.Model):
	title = models.CharField(max_length=20, null=False, help_text='板块名')
	parent = models.IntegerField(null=False, help_text='上级目录')
	grade = models.IntegerField(null=False, help_text='级别')


