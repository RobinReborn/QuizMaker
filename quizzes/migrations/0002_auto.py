# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field result on 'Question'
        db.delete_table(db.shorten_name(u'quizzes_question_result'))


    def backwards(self, orm):
        # Adding M2M table for field result on 'Question'
        m2m_table_name = db.shorten_name(u'quizzes_question_result')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm[u'quizzes.question'], null=False)),
            ('result', models.ForeignKey(orm[u'quizzes.result'], null=False))
        ))
        db.create_unique(m2m_table_name, ['question_id', 'result_id'])


    models = {
        u'quizzes.question': {
            'Meta': {'object_name': 'Question'},
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['quizzes.Question']", 'null': 'True', 'blank': 'True'}),
            'results': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['quizzes.Result']", 'null': 'True', 'blank': 'True'})
        },
        u'quizzes.result': {
            'Meta': {'object_name': 'Result'},
            'Quiz_Result': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Quiz_Result_Explanation': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Quiz_Scoring': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['quizzes']