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
	data['user'] = request.user.username

	if request.method == "POST" and request.is_ajax:

		#form  = LessonForm(request.POST)
		exercise_uri = request.POST['exercise_uri']
		solution = request.POST['solution']

		print exercise_uri
		print solution
		#exercise = Exercise.objects.get(pk=exercise_id)
		exercise = Exercise.objects.order_by('last_correct')[0]
		data['result'] = exercise.validate(solution)


	return HttpResponse(json.dumps(data),mimetype='application/json')



def exercise(request):
	exercise = None
	data = {}
	try:
		#Recover the next exercise.
		#Convert it into data dictionary and return httresponse
		exercise = Exercise.objects.order_by('last_correct')[0]
		return HttpResponse(json.dumps(exercise.to_json()),mimetype='application/json')

	except:
		print 'exception'
		data['exercise'] = None
		return HttpResponse(json.dumps(data),mimetype='application/json')


def exercises(request):
	data = []
	exercises = Exercise.objects.order_by('last_correct')
	for exercise in exercises:
		data.append(exercise.to_json())

	return HttpResponse(json.dumps(data), mimetype='application/json')
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
