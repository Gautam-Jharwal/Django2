# Generated by Django 4.0.6 on 2022-07-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_students_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Assignment_ID', models.IntegerField(default='SOME STRING')),
                ('Teacher_ID', models.IntegerField(default='SOME STRING')),
                ('Student_Roll_no', models.IntegerField(default='SOME STRING')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_ID', models.IntegerField(default='SOME STRING')),
                ('Course_name', models.CharField(default='SOME STRING', max_length=100)),
                ('Students_ID', models.CharField(default='SOME STRING', max_length=100)),
                ('Course_Price', models.IntegerField(default='SOME STRING')),
                ('Course_Description', models.CharField(default='SOME STRING', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_ID', models.IntegerField(default='SOME STRING')),
                ('Teacher_ID', models.IntegerField(default='SOME STRING')),
                ('Employee_Designation', models.CharField(default='SOME STRING', max_length=200)),
                ('Employee_Salary', models.IntegerField(default='SOME STRING')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Result_ID', models.IntegerField(default='SOME STRING')),
                ('Students_ID', models.CharField(default='SOME STRING', max_length=100)),
                ('Marks_Obtained', models.IntegerField(default='SOME STRING')),
                ('Remark', models.CharField(default='SOME STRING', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_ID', models.IntegerField(default='SOME STRING')),
                ('Teacher_Name', models.CharField(max_length=100)),
                ('Teacher_Phone', models.IntegerField(default='SOME STRING')),
                ('Course_ID', models.IntegerField(default='SOME STRING')),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='Student_Name',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='students',
            name='Student_Phoneno',
            field=models.IntegerField(default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='students',
            name='Student_Roll_no',
            field=models.IntegerField(default='SOME STRING'),
        ),
    ]
