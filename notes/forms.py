from django.forms import ModelForm
from .models import NOTES


class NOTEForm(ModelForm):
    class Meta:
        model = NOTES
        fields = ['title', 'content']
