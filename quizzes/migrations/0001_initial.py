# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quiz'
        db.create_table(u'quizzes_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Quiz_Title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Quiz_Description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'quizzes', ['Quiz'])

        # Adding model 'Question'
        db.create_table(u'quizzes_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('answer1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('answer2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('answer3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('answer4', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Quiz_Part', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['quizzes.Quiz'])),
        ))
        db.send_create_signal(u'quizzes', ['Question'])

        # Adding model 'Result'
        db.create_table(u'quizzes_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Quiz_Results', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['quizzes.Quiz'])),
            ('Quiz_Scoring', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=100)),
            ('Quiz_Result', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Quiz_Result_Explanation', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'quizzes', ['Result'])


    def backwards(self, orm):
        # Deleting model 'Quiz'
        db.delete_table(u'quizzes_quiz')

        # Deleting model 'Question'
        db.delete_table(u'quizzes_question')

        # Deleting model 'Result'
        db.delete_table(u'quizzes_result')


    models = {
        u'quizzes.question': {
            'Meta': {'object_name': 'Question'},
            'Quiz_Part': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['quizzes.Quiz']"}),
            'answer1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'answer2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'answer3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'answer4': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'quizzes.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'Quiz_Description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Quiz_Title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'quizzes.result': {
            'Meta': {'object_name': 'Result'},
            'Quiz_Result': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Quiz_Result_Explanation': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Quiz_Results': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['quizzes.Quiz']"}),
            'Quiz_Scoring': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['quizzes']