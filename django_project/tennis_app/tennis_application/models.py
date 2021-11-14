from django.db import models

class Player(models.Model):
	player_id = models.PositiveIntegerField(primary_key=True)
	name     = models.CharField(max_length=15)
	family   = models.CharField(max_length=30)
	birthday = models.DateTimeField()
	count_wons = models.PositiveIntegerField()
	sex = models.BinaryField()

class Sponsor(models.Model):
	sponsor_id = models.PositiveIntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	players = models.ManyToManyField(Player)

class Tournament(models.Model):
	tournament_id = models.PositiveIntegerField(primary_key=True)
	name      = models.CharField(max_length=50)
	begin_tur = models.DateTimeField()
	end_tur   = models.DateTimeField()
	category  = models.CharField(max_length=15)
	sponsors  = models.ManyToManyField(Sponsor)
	players   = models.ManyToManyField(Player)