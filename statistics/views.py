# Create your views here.
from lessons.models import Exercise
from collections import Counter
import re
import json
from django.http import HttpResponse

def get_values(request):
	exercises = Exercise.objects.all()
	counter = Counter()
	for exercise in exercises:
		ratio = exercise.corrects/float(exercise.tries)
		if ratio > 0.5:
			words = re.findall(r"\w+", exercise.translation.es, re.UNICODE)
			for word in words:
				counter[word.lower()] += 1
	data  = []
	for index,value in counter.most_common(10):
		data.append([index,value])

	return HttpResponse(json.dumps(data), mimetype='application/json')
