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

        # Adding M2M table for field questions on 'Quiz'
        m2m_table_name = db.shorten_name(u'quizzes_quiz_questions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quiz', models.ForeignKey(orm[u'quizzes.quiz'], null=False)),
            ('question', models.ForeignKey(orm[u'quizzes.question'], null=False))
        ))
        db.create_unique(m2m_table_name, ['quiz_id', 'question_id'])

        # Adding M2M table for field results on 'Quiz'
        m2m_table_name = db.shorten_name(u'quizzes_quiz_results')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quiz', models.ForeignKey(orm[u'quizzes.quiz'], null=False)),
            ('result', models.ForeignKey(orm[u'quizzes.result'], null=False))
        ))
        db.create_unique(m2m_table_name, ['quiz_id', 'result_id'])

        # Adding model 'Question'
        db.create_table(u'quizzes_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('answer1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('answer2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('answer3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('answer4', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'quizzes', ['Question'])

        # Adding M2M table for field result on 'Question'
        m2m_table_name = db.shorten_name(u'quizzes_question_result')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm[u'quizzes.question'], null=False)),
            ('result', models.ForeignKey(orm[u'quizzes.result'], null=False))
        ))
        db.create_unique(m2m_table_name, ['question_id', 'result_id'])

        # Adding model 'Result'
        db.create_table(u'quizzes_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Quiz_Scoring', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=100)),
            ('Quiz_Result', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Quiz_Result_Explanation', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'quizzes', ['Result'])


    def backwards(self, orm):
        # Deleting model 'Quiz'
        db.delete_table(u'quizzes_quiz')

        # Removing M2M table for field questions on 'Quiz'
        db.delete_table(db.shorten_name(u'quizzes_quiz_questions'))

        # Removing M2M table for field results on 'Quiz'
        db.delete_table(db.shorten_name(u'quizzes_quiz_results'))

        # Deleting model 'Question'
        db.delete_table(u'quizzes_question')

        # Removing M2M table for field result on 'Question'
        db.delete_table(db.shorten_name(u'quizzes_question_result'))

        # Deleting model 'Result'
        db.delete_table(u'quizzes_result')


    models = {
        u'quizzes.question': {
            'Meta': {'object_name': 'Question'},
            'answer1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'answer2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'answer3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'answer4': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'result': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quizzes.Result']", 'symmetrical': 'False'})
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
