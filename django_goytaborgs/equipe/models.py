from django.db import models
from django.contrib.auth.models import User

# Modelo de Equipe
class Team(models.Model):
    name = models.CharField(max_length=100)
    captain = models.ForeignKey('Competitor', related_name='captained_teams', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

# Modelo de Competidor
class Competitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='members', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.user.username

    # Método para verificar se é capitão da equipe
    def is_captain(self):
        return self.team and self.team.captain == self

# Modelo de Robô
class Robot(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='robots/')
    team = models.ForeignKey(Team, related_name='robots', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
