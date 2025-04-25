from django.db import models

# 3. lets create a model that represents a teacher
class Teacher(models.Model):
    # name of the teacher
    name = models.CharField(max_length=100)

    # subject they teach
    subject = models.CharField(max_length=100)

    # this makes it easier to see the course name in django admin or shell
    def __str__(self):
        return self.name

#1. Lets create a model that reprents a course that students can be enrolled in
class Course(models.Model):
    # name of the course e.g. math 101
    title = models.CharField(max_length=100)

    # optional description of the course
    description = models.TextField(blank=True)

    # links to step 3 lets connect a course to a teacher
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    # this makes it easier to see the course name in django admin or shell
    def __str__(self):
        return self.title
    
# 2. Lets create a model that represents a student
class Student(models.Model):
    # Name of the student
    name = models.CharField(max_length=100)

    # description
    des = models.TextField()

    # ForeignKey creates a many to one relationship to course
    # this means many students can be enrolled in one course
    #this connects each student to one course, if a course is deleted any students in that course are deleted
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

     # this makes it easier to see the course name in django admin or shell
    def __str__(self):
        return self.name
    

# 4. lets make a class to represent mlb indiviual players
class Player(models.Model):
    # name of player
    name = models.CharField(max_length=100)
    #postion
    position = models.CharField(max_length=100)
    # batting average
    batting_average = models.FloatField
    def __str__(self):
        return self.name

    

