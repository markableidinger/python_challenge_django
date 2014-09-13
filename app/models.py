from django.db import models
from django.forms import ModelForm

class User(models.Model):
    first = models.CharField(max_length = 50)
    last = models.CharField(max_length = 50) or ''
    email = models.EmailField(max_length = 50)
    def __str__(self):
        return '{} {}'.format(self.first, self.last)

class Edit_Form(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

