# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Answer.answerNumber'
        db.add_column(u'quizzes_answer', 'answerNumber',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Answer.answerNumber'
        db.delete_column(u'quizzes_answer', 'answerNumber')


    models = {
        u'quizzes.answer': {
            'Meta': {'object_name': 'Answer'},
            'answerNumber': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'answertext': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quizzes.Question']", 'null': 'True', 'blank': 'True'})
        },
        u'quizzes.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100'}),
            'num_answers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'questionNumber': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'quizzes.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'Quiz_Description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Quiz_Title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Quiz_Type': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['quizzes.Question']", 'null': 'True', 'blank': 'True'}),
            'results': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['quizzes.Result']", 'null': 'True', 'blank': 'True'}),
            'timesTaken': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'quizzes.result': {
            'Meta': {'object_name': 'Result'},
            'Quiz_Result': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Quiz_Result_Explanation': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Quiz_Scoring': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100'}),
            'resultNumber': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['quizzes']