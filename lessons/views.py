# Create your views here.
from lessons.models import Exercise, LessonForm, DialogueSentence
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt

#todo:remove this decorator
@csrf_exempt
def submit_solution(request):
	data = {'result':False}

	if request.method == "POST" and request.is_ajax:

		form  = LessonForm(request.POST)
		solution = form['solution'].value()
		
		#exercise = Exercise.objects.get(pk=exercise_id)
		exercise = Exercise.objects.order_by('last_correct')[0]
		result = exercise.validate(solution)
		
		data['result'] = result
		
	return HttpResponse(json.dumps(data),mimetype='application/json')
	
def dialogue(request):
	dialogues = DialogueSentence.objects.order_by('seq_num')
	return render_to_response("lesson/exercise/dialogue/lesson.html",{'dialogues':dialogues})

def exercise(request):
	exercise = None
	data = {}
	try:
		
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
	return render_to_response("lesson/exercise/translation/list.html", {'exercises':exercises}, context_instance=RequestContext(request))

def train(request):
	exercises = Exercise.objects.order_by('last_correct')
	exercise = exercises[0]

	if request.method == 'GET':

		succeded = request.session.get('succed')
		form = LessonForm()
		c = {'form': form,'exercise':exercise,'exercises':exercises, 'success':succeded}
		return render_to_response("lesson/exercise/translation/lesson.html", c, context_instance=RequestContext(request))

	else:
		form = LessonForm()	
		c = {'form': form,'exercise':exercise,'exercises':exercises}
		return render_to_response("lesson/exercise/translation/lesson.html", c, context_instance=RequestContext(request))


def results(request):
	exercises = Exercise.objects.all()
	return render_to_response('lesson/exercise/translation/list.html',{'exercises':exercises})

	