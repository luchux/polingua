from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie import fields 
from lessons.models import Translation,Exercise

class TranslationResource(ModelResource):
    class Meta:
        queryset = Translation.objects.all()
	
	def dehydrate(self, bundle):
		bundle['a'] = 1
		return bundle
 	

class ExerciseResource(ModelResource):
	translation = fields.ToOneField(TranslationResource, 'translation',full=True)

	class Meta:
		queryset = Exercise.objects.order_by('last_correct') 
