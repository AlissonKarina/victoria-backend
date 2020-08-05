from django.db import models

# Create your models here.
class AnswerQuestion (models.Model):
    answer_text = models.TextField()
    question = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

class Paper (models.Model):
    title = models.CharField(max_length = 400)
    authors = models.CharField(max_length = 400)
    year = models.IntegerField()
    treatment = models.CharField(max_length = 200)
    description = models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to='papers', null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.id) + "-" + self.title

class AnswerText (models.Model):
    answer_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    paper = models.ForeignKey(Paper, related_name='answer_texts', on_delete=models.CASCADE)

    def __str__(self):
        return self.paper.title + "-" + str(self.id)

class Parameter (models.Model):
    keratometry = models.DecimalField(max_digits=4, decimal_places=2)
    pachymetry = models.DecimalField(max_digits=4, decimal_places=2)
    cdva = models.DecimalField(max_digits=4, decimal_places=2)
    udva = models.DecimalField(max_digits=4, decimal_places=2)
    grade = models.IntegerField()

    def __str__(self):
        return self.keratometry

class Question (models.Model):
    question = models.TextField()
    answer = models.TextField(max_length = 400, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    parameter = models.ForeignKey(Parameter, related_name='parameters', on_delete=models.CASCADE)
    answer_text = models.ManyToManyField(AnswerText, related_name='answer_texts')

    def __str__(self):
        return self.question




