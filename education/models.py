from django.db import models

class Course(models.Model):
    image=models.ImageField(upload_to='Images/course')
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()



    def __str__(self):
        return self.title

class Student(models.Model):
    image=models.ImageField(upload_to='Images/student')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    phone=models.TextField()
    email = models.EmailField()
    id_card = models.TextField()



    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    image=models.ImageField(upload_to='Images/teachers')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.TextField()
    email = models.EmailField()
    id_card = models.TextField()
    experience = models.TextField(null=True)
    sertificate = models.TextField(null=True)

    def __str__(self):
        return self.first_name



class Group(models.Model):
    image=models.ImageField(upload_to='Images/group')
    title = models.CharField(max_length=150)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    room=models.PositiveIntegerField()
    study_time = models.TimeField()
    study_days=models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title
