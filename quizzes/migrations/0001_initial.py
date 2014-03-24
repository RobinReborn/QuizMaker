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
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('timesTaken', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('Quiz_Type', self.gf('django.db.models.fields.CharField')(max_length=1000)),
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
            ('num_answers', self.gf('django.db.models.fields.IntegerField')()),
            ('questionNumber', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'quizzes', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'quizzes_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quizzes.Question'], null=True, blank=True)),
            ('answertext', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'quizzes', ['Answer'])

        # Adding model 'Result'
        db.create_table(u'quizzes_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Quiz_Scoring', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=100)),
            ('Quiz_Result', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('resultNumber', self.gf('django.db.models.fields.IntegerField')()),
            ('Quiz_Result_Explanation', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
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

        # Deleting model 'Answer'
        db.delete_table(u'quizzes_answer')

        # Deleting model 'Result'
        db.delete_table(u'quizzes_result')


    models = {
        u'quizzes.answer': {
            'Meta': {'object_name': 'Answer'},
            'answertext': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quizzes.Question']", 'null': 'True', 'blank': 'True'})
        },
        u'quizzes.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'num_answers': ('django.db.models.fields.IntegerField', [], {}),
            'questionNumber': ('django.db.models.fields.IntegerField', [], {}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'quizzes.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'Quiz_Description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Quiz_Title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Quiz_Type': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'resultNumber': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['quizzes']