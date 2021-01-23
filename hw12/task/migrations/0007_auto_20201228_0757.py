# Generated by Django 3.1.4 on 2020-12-28 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20201227_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeworkResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework', models.CharField(max_length=200)),
                ('solution', models.TextField()),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='HomeworkTable',
            new_name='Homework',
        ),
        migrations.RenameModel(
            old_name='StudentsTable',
            new_name='Teachers',
        ),
        migrations.RenameModel(
            old_name='TeachersTable',
            new_name='Students',
        ),
        migrations.DeleteModel(
            name='HomeworkResultTable',
        ),
        migrations.AddField(
            model_name='homeworkresult',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='task.students'),
        ),
    ]