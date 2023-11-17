from django.db import models


class Conference (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='teams', null=True, blank=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    wins = models.CharField(max_length=100)
    losses = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    injured_res_list = models.BooleanField(default=False)
    number = models.CharField(max_length=100)
    college = models.CharField(max_length=100)

    def __str__(self):
        return self.name


