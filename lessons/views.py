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

	if request.method == "POST" and request.is_ajax:

		data = {'result':False}
		data['user'] = request.user.username

		#exercise_uri = request.POST['exercise_uri']
		solution = request.POST['solution']

		#exercise = Exercise.objects.get(pk=exercise_id)
		exercise = Exercise.objects.order_by('last_correct')[0]
		data['result'] = exercise.validate(solution)

		return HttpResponse(json.dumps(data),mimetype='application/json')
	else:
		#TODO: checkear
		return train(request)

## Version 1 ##
@login_required(login_url='/accounts/login/')
def train(request):

	#List of exercises with the first exercise
	exercises = Exercise.objects.order_by('last_correct')
	exercise = exercises[0]
	c = {'exercise':exercise,'exercises':exercises}
	return render_to_response("lesson/exercise/translation/lesson.html", c,context_instance=RequestContext(request))

