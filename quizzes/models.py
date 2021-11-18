from django.db import models

class Quiz(models.Model):
    
    name = models.CharField(max_length = 80)
    description = models.CharField(max_length = 300)
    num_questions = models.IntegerField(default = 10)
    slug = models.SlugField(max_length = 20)
    img = models.URLField(blank = True) # allow it to be none

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):

    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    img = models.URLField(blank = True) # allow none`
    content = models.CharField(max_length = 200)

    op0 = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.content
    
    def get_answers(self):
        return self.answer_set.all()

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    content = models.CharField(max_length = 200)
    correct = models.BooleanField(default = False)

    def __str__(self):
        return self.content
    

# https://stackoverflow.com/questions/6928692/how-to-express-a-one-to-many-relationship-in-django
