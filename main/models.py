from django.db import models
from django.contrib.auth.models import AbstractUser


# ----------- JOB CHOICES -----------
class JobChoices(models.TextChoices):
	'''A class that indicates the player's job or specialization.'''
	INITIATE = "INITIATE", "Initiate (Beginner)"
	WARRIOR = "WARRIOR", "Warrior (Fighter)"
	TITAN = "TITAN", "Titan (Overcame Limits)"
	SHADOW = "SHADOW", "Shadow (Invisible Master)"
	PRIME = "PRIME", "Prime (Absolute Discipline)"


# ----------- MODE CHOICES -----------
class ModeChoices(models.TextChoices):
	'''Indicates which mode the player is in.'''
	DRAKON = "DRAKON", "Ultra Intensity, relentless execution"
	TERMINATOR = "TERMINATOR", "No emotions, just execution"
	SPARTAN = "SPARTAN", "Mental and physical discipline"
	GHOST = "GHOST", "Silent mode, no distractions"
	GENIUS = "GENIUS", "Maximum knowledge absorption"


# ----------- PLAYER MODEL -----------
class Player(AbstractUser):
	'''Player model that extends the Django AbstractUser.'''

	class Meta:
		verbose_name = 'Player'
		verbose_name_plural = 'Players'

	level = models.PositiveIntegerField(default=0, blank=True)  # player level
	job = models.CharField(max_length=10, choices=JobChoices.choices, default=JobChoices.INITIATE)  # player job
	mode = models.CharField(max_length=20, choices=ModeChoices.choices, blank=True, null=True)  # player mode

	hp = models.IntegerField(default=0, blank=True)  # health point
	mp = models.IntegerField(default=0, blank=True)  # mana point
	xp = models.IntegerField(default=0, blank=True)  # experience point

	artifacts = models.JSONField(default=dict, blank=True, null=True)  # artifacts

	gold = models.PositiveIntegerField(default=0, blank=True, null=True)  # gold
	fatigue = models.PositiveIntegerField(default=0, blank=True, null=True)  # fatigue

	str_v = models.PositiveIntegerField(default=0, blank=True, null=True)  # strength
	agi_v = models.PositiveIntegerField(default=0, blank=True, null=True)  # agility
	per_v = models.PositiveIntegerField(default=0, blank=True, null=True)  # perception
	vit_v = models.PositiveIntegerField(default=0, blank=True, null=True)  # vitality
	int_v = models.PositiveIntegerField(default=0, blank=True, null=True)  # intelligence

	def __str__(self):
		return f'{self.username} - (job: {self.get_job_display()}, level: {self.level})'


	# ----------- ARTIFACT -----------
	def add_artifact(self, name, power, description='No description'):
		'''Add an artifact to the player's collection.'''
		if not isinstance(self.artifacts, dict):
			self.artifacts = {}

		self.artifacts[name] = {'power': power, 'description': description}
		self.save()

	def remove_artifact(self, name):
		'''Remove an artifact from the player's collection.'''
		if name in self.artifacts:
			del self.artifacts[name]
			self.save()
			return True
		return False


	# ----------- GOLD METHODS -----------
	def add_gold(self, amount):
		'''Increase the player's gold.'''
		if amount > 0:
			self.gold += amount
			self.save()

	def spend_gold(self, amount):
		'''Decrease the player's gold if sufficient balance exists.'''
		if 0 < amount <= self.gold:
			self.gold -= amount
			self.save()
			return True
		return False