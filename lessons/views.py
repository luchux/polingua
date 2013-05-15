# Create your views here.
from lessons.models import Exercise, LessonForm, DialogueSentence
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
import json

from django.views.decorators.csrf import csrf_exempt

#todo:remove this decorator
@csrf_exempt
@login_required(login_url='/accounts/login/')

def submit_solution(request):
	data = {'result':False}

	if request.method == "POST" and request.is_ajax:

		form  = LessonForm(request.POST)
		solution = form['solution'].value()

		#exercise = Exercise.objects.get(pk=exercise_id)
		exercise = Exercise.objects.order_by('last_correct')[0]
		correct = exercise.validate(solution)

		if correct:
			user = request.user


		data['result'] = correct
		data['user'] = user.username

	return HttpResponse(json.dumps(data),mimetype='application/json')


def exercise(request):
	exercise = None
	data = {}
	try:
		#Recover the next exercise.
		#Convert it into data dictionary and return httresponse
		exercise = Exercise.objects.order_by('last_correct')[0]
		data['exercise'] = {'trans_es':exercise.translation.es,
							'trans_en':exercise.translation.en,
							'urls':exercise.translation.img_urls.split("URLURL"),
		}

		return HttpResponse(json.dumps(data),mimetype='application/json')

	except:

		data['exercise'] = None
		return HttpResponse(json.dumps(data),mimetype='application/json')


def exercises(request):
	exercises = Exercise.objects.order_by('last_correct')
	return render_to_response("lesson/exercise/words/exercises.html", {'exercises':exercises}, context_instance=RequestContext(request))

## version 2 ##
@login_required(login_url='/accounts/login/')
def words_training(request):

	#List of exercises with the first exercise
	exercises = Exercise.objects.order_by('last_correct')
	exercise = exercises[0]

	if request.method == 'GET':
		#Data is comming from a get method ajax probably

		form = LessonForm()
		c = {'form': form,'exercise':exercise,'exercises':exercises}
		return render_to_response("lesson/exercise/words/index.html", c, context_instance=RequestContext(request))

	else:
		form = LessonForm()
		c = {'form': form,'exercise':exercise,'exercises':exercises}
		return render_to_response("lesson/exercise/words/index.html", c, context_instance=RequestContext(request))

## Version 1 ##
@login_required(login_url='/accounts/login/')
def train(request):

	#List of exercises with the first exercise
	exercises = Exercise.objects.order_by('last_correct')
	exercise = exercises[0]

	if request.method == 'GET':
		#Data is comming from a get method ajax probably

		form = LessonForm()
		c = {'form': form,'exercise':exercise,'exercises':exercises}
		return render_to_response("lesson/exercise/translation/lesson.html", c, context_instance=RequestContext(request))

	else:
		form = LessonForm()
		c = {'form': form,'exercise':exercise,'exercises':exercises}
		return render_to_response("lesson/exercise/translation/lesson.html", c, context_instance=RequestContext(request))


'''
def dialogue(request):
	#dialogues = DialogueSentence.objects.order_by('seq_num')
	return render_to_response("lesson/exercise/dialogue/index.html")

def results(request):
	exercises = Exercise.objects.all()
	return render_to_response('lesson/exercise/translation/list.html',{'exercises':exercises})
'''
