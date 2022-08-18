
from .models import Subject
from bootstrap_modal_forms.forms import BSModalModelForm

class SubjectModelForm(BSModalModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'neptun', 'professor']