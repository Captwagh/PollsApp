from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=500)
    publish_date = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.question)


class Choice(models.Model):
    choice = models.CharField(max_length=500)
    # This basically allows Choice class to access attributes of Primary Table via Foreign Key
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.choice} | {self.question}"
