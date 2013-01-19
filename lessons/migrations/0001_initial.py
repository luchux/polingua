# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sentence'
        db.create_table('lessons_sentence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('es', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('en', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('lessons', ['Sentence'])

        # Adding model 'Translation'
        db.create_table('lessons_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('es', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('en', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('img_urls', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('lessons', ['Translation'])

        # Adding model 'Exercise'
        db.create_table('lessons_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('translation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lessons.Translation'])),
            ('tries', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('corrects', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('last_correct', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('lessons', ['Exercise'])

        # Adding model 'Speaker'
        db.create_table('lessons_speaker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
        ))
        db.send_create_signal('lessons', ['Speaker'])

        # Adding model 'DialogueSentence'
        db.create_table('lessons_dialoguesentence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sentence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lessons.Translation'])),
            ('speaker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lessons.Speaker'])),
            ('seq_num', self.gf('django.db.models.fields.IntegerField')(max_length=200)),
        ))
        db.send_create_signal('lessons', ['DialogueSentence'])

        # Adding model 'Dialogue'
        db.create_table('lessons_dialogue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num_speakers', self.gf('django.db.models.fields.IntegerField')(max_length=20)),
        ))
        db.send_create_signal('lessons', ['Dialogue'])

        # Adding M2M table for field sentences on 'Dialogue'
        db.create_table('lessons_dialogue_sentences', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dialogue', models.ForeignKey(orm['lessons.dialogue'], null=False)),
            ('dialoguesentence', models.ForeignKey(orm['lessons.dialoguesentence'], null=False))
        ))
        db.create_unique('lessons_dialogue_sentences', ['dialogue_id', 'dialoguesentence_id'])

        # Adding model 'Lesson'
        db.create_table('lessons_lesson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('lessons', ['Lesson'])

        # Adding M2M table for field exercises on 'Lesson'
        db.create_table('lessons_lesson_exercises', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['lessons.lesson'], null=False)),
            ('exercise', models.ForeignKey(orm['lessons.exercise'], null=False))
        ))
        db.create_unique('lessons_lesson_exercises', ['lesson_id', 'exercise_id'])


    def backwards(self, orm):
        # Deleting model 'Sentence'
        db.delete_table('lessons_sentence')

        # Deleting model 'Translation'
        db.delete_table('lessons_translation')

        # Deleting model 'Exercise'
        db.delete_table('lessons_exercise')

        # Deleting model 'Speaker'
        db.delete_table('lessons_speaker')

        # Deleting model 'DialogueSentence'
        db.delete_table('lessons_dialoguesentence')

        # Deleting model 'Dialogue'
        db.delete_table('lessons_dialogue')

        # Removing M2M table for field sentences on 'Dialogue'
        db.delete_table('lessons_dialogue_sentences')

        # Deleting model 'Lesson'
        db.delete_table('lessons_lesson')

        # Removing M2M table for field exercises on 'Lesson'
        db.delete_table('lessons_lesson_exercises')


    models = {
        'lessons.dialogue': {
            'Meta': {'object_name': 'Dialogue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_speakers': ('django.db.models.fields.IntegerField', [], {'max_length': '20'}),
            'sentences': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lessons.DialogueSentence']", 'symmetrical': 'False'})
        },
        'lessons.dialoguesentence': {
            'Meta': {'object_name': 'DialogueSentence'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lessons.Translation']"}),
            'seq_num': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lessons.Speaker']"})
        },
        'lessons.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'corrects': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_correct': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lessons.Translation']"}),
            'tries': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'lessons.lesson': {
            'Meta': {'object_name': 'Lesson'},
            'exercises': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lessons.Exercise']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'lessons.sentence': {
            'Meta': {'object_name': 'Sentence'},
            'en': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'es': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lessons.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'gender': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'lessons.translation': {
            'Meta': {'object_name': 'Translation'},
            'en': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'es': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_urls': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['lessons']