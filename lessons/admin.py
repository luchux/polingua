from django.contrib import admin
from lessons.models import Translation, Exercise, Lesson, Speaker, \
 Dialogue, DialogueSentence, Sentence, ExerciseSentence

admin.site.register(ExerciseSentence)
admin.site.register(Sentence)
admin.site.register(Translation)
admin.site.register(Exercise)
admin.site.register(Lesson)
admin.site.register(Speaker)
admin.site.register(Dialogue)
admin.site.register(DialogueSentence)
