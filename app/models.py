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
    batting_average = models.FloatField(default=0.0)
    #
    # lets add make a relationship between a player and team so a player can be asigned to only one team
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='players', null=True, blank=True)
    #ForeignKey('Team'): Links the player to a team.

    #on_delete=models.CASCADE: If a team is deleted, all its players get deleted too.

    #related_name='players': Lets you do team.players.all() to get all players on a team.
    def __str__(self):
        return self.name

    
# 5. lets make a class for teams
class Team(models.Model):
    #name
    name = models.CharField(max_length=100)
    # city
    city = models.CharField(max_length=100)
    # manager
    manager = models.CharField(max_length=100)
    # League can be "AL" (American League) or "NL" (National League)
    league = models.CharField(max_length=2)
    def __str__(self):
        # When shown in admin, it will appear as "New York Yankees" so name then city
        return f"{self.city} {self.name}"
    
# Lets make a class for caddies
class Caddie(models.Model):
    #name
    name = models.CharField(max_length=100)
    # bib
    bib_color = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

# lets make a class for members at the club
class Member(models.Model):
    #name
    name = models.CharField(max_length=100)
    # handicap
    handicap = models.FloatField(default=0.0)
    # assign a caddie, this means a caddie can be assigheed to multiple members
    caddie = models.ForeignKey(Caddie, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name
    

# lets  create a model for time slots
class Timeslot(models.Model):
    # times
    times = models.CharField(max_length=100)
    def __str__(self):
        return self.times

# lets connect a member to a timeslot, this is like book keeping
class MemberTeeTime(models.Model):
    # lets connect to which member
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    # lets connect to a timeslot
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.member.name} - {self.timeslot.times}"