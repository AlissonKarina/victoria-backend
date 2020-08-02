from django.db import models

# Create your models here.
class AnswerQuestion (models.Model):
    answer_text = models.TextField()
    question = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

""" class Paper (models.Model):
    title = models.CharField()
    authors = models.CharField()
    description = models.TextField()
    pdf = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return self.title """

""" class AnswerText (models.Model):
    answer_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    id_paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_paper.title + self.id """
    
""" class AnswerQuestion (models.Model):
    id_answer_text = models.ForeignKey(AnswerText, on_delete=models.CASCADE)
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_answer_text.id_paper.title + " - " + self.id_question.question """

""" class Question (models.Model):
    question = models.CharField(max_length = 500)
    answer = models.TextField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question """




