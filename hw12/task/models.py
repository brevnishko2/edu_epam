from django.db import models


# Create your models here.
class Teachers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Homework(models.Model):
    text = models.TextField()
    deadline_days = models.IntegerField()
    created = models.DateTimeField()
    create_by = models.CharField(max_length=200, default="Unknown Teacher")


class HomeworkResult(models.Model):
    homework = models.CharField(max_length=200)
    solution = models.TextField()
    author = models.OneToOneField(Students, on_delete=models.CASCADE)
    created = models.DateTimeField()


class HomeworksDone(models.Model):
    homework = models.OneToOneField(
        Homework, on_delete=models.CASCADE, primary_key=True
    )
    done_by = models.TextField()
    create_by = models.CharField(max_length=200)
