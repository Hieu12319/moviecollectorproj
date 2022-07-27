from django.forms import ModelForm
from .models import Ratings

class RatingsForm(ModelForm):
    class Meta:
        model = Ratings
        fields = ['thoughts', 'rate']

    def __str__(self):
        return f"{self.get_rate_display()} on {self.thoughts}"