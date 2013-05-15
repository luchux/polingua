from django.db import models
from datetime import datetime
from django import forms
import requests

# ---- Class Sentence ------------------------#
class Sentence(models.Model):
	es = models.CharField('es',max_length=200)
	en = models.CharField('en',max_length=200)

	def __unicode__(self):
		try:
			return self.en[:15]
		except:
			return self.en


# ---- Class Translation ------------------------#
class Translation(models.Model):
	es = models.CharField('es',max_length=200)
	en = models.CharField('en',max_length=200)
	img_urls = models.TextField('url',blank=True)

	def __unicode__(self):
		return self.en

#ToDo: a model for images.
#class ImageExercise(models.Model):
	def load_images(self):

		query = self.en
		url_api = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="+query

		try:
			response = requests.get(url_api)
			json_resp = response.json()
			img_results = json_resp['responseData']['results']
			images_urls = []

			for res in img_results:
				img_url = res['tbUrl']
				images_urls.append(img_url)
				if len(images_urls) == 3:
					break;

			self.img_urls = 'URLURL'.join(images_urls)

		except:
			self.img_urls = []
			return



	def save(self, *args, **kwargs):
		#if is the first time the object is created, we retrieve images, store in static,
		# and call save() of father.
		#else call save() father.
		if not self.pk:
			self.load_images()
			super(Translation, self).save(*args, **kwargs) # Call the "real" save() method.
		else:
			super(Translation, self).save(*args, **kwargs) # Call the "real" save() method.

	def get_urls(self):
		if self.img_urls:
			return self.img_urls.split('URLURL')
	#do_something_else()

#ToDo: this class should be renamed to ExerciseWords?

class ExerciseBase(models.Model):
	tries = models.IntegerField(blank=True,default=0)
	corrects = models.IntegerField(blank=True,default=0)
	last_correct = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True)

	def validate(self,instance):
		pass


class ExerciseSentence(models.Model):
	sentence = models.ForeignKey(Sentence)
	level = models.IntegerField(blank=True,default=1)

	tries = models.IntegerField(blank=True,default=0)
	corrects = models.IntegerField(blank=True,default=0)
	last_correct = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True)

	def __unicode__(self):
		return u"Exercise "+str(self.pk)

	def validate(self,input_text):
		#lets add statistics and validate the answer
		self.tries = self.tries + 1

		if self.sentence.es == input_text:
			self.last_correct = datetime.now()
			self.corrects = self.corrects + 1
			self.save()
			return True
		else:
			self.save()
			return False



# ---- Class Exercise ------------------------#
class Exercise(models.Model):
	translation = models.ForeignKey(Translation)
	#user
	tries = models.IntegerField(blank=True,default=0)
	corrects = models.IntegerField(blank=True,default=0)
	last_correct = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True)
	#ToDO: add score as attribute, and more stats. They are being processed
	#now out of the model.

	#img = models.FileField(upload_to='imgs/',blank=True)

	def __unicode__(self):
		return u"Exercise "+str(self.pk)

	def validate(self, input_text):
		#lets add statistics and validate the answer
		self.tries = self.tries + 1

		if self.translation.es == input_text:
			self.last_correct = datetime.now()
			self.corrects = self.corrects + 1
			self.save()
			return True
		else:
			self.save()
			return False

	def to_json(self):
		return {'trans_es': self.translation.es,
				'trans_en': self.translation.en,
				'url': self.translation.img_urls}


#ToDo: check if Exercise can be a father class of dialogue and translation.
'''
class DialogueExercise(models.Model):
	dialogues = models.ManyToManyField(DialogueSentence)
'''
#Represent the Dialogues that are part of exercises for training and test.
#A Dialogue is a set of Lists of Transletion. i.e. A Speaker, is represented
# as a list of Translations.

GENDER_CHOICES = ((0, 'Male'), (1, 'Female'),(2,'NoIdea'))

# ---- Class Speaker ------------------------#
class Speaker(models.Model):
	name = models.CharField('name',max_length=20)
	gender = models.IntegerField('gender',max_length=2, choices = GENDER_CHOICES)

	def __unicode__(self):
		return self.name

# ---- Class DialogueSentence ------------------------#
class DialogueSentence(models.Model):
	sentence = models.ForeignKey(Sentence)
	speaker = models.ForeignKey(Speaker)
	seq_num = models.IntegerField('seq_num',max_length = 200)

	def __unicode__(self):
		return self.speaker.name + ' - ' + self.sentence.__unicode__()

# ---- Class Dialogue ------------------------#
class Dialogue(models.Model):
	num_speakers = models.IntegerField('num_speakers', max_length = 20)
	sentences = models.ManyToManyField(DialogueSentence)

#General Lessons
class Lesson(models.Model):
	name = models.CharField('name',max_length=200)
	exercises = models.ManyToManyField(Exercise)


class LessonForm(forms.Form):
	solution = forms.CharField()

