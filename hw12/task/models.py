from django.db import models


# Create your models here.
class TeachersTable(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class StudentsTable(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class HomeworkTable(models.Model):
    text = models.TextField()
    deadline_days = models.IntegerField()
    created = models.DateTimeField()
    create_by = models.CharField(max_length=200, default="Unknown Teacher")


class HomeworkResultTable(models.Model):
    homework = models.OneToOneField(HomeworkTable, on_delete=models.CASCADE)
    solution = models.TextField()
    author = models.CharField(max_length=200)
    created = models.DateTimeField()


class HomeworksDone(models.Model):
    homework = models.OneToOneField(
        HomeworkTable, on_delete=models.CASCADE, primary_key=True
    )
    done_by = models.TextField()
    create_by = models.CharField(max_length=200)
