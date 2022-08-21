from .models import Hello
from django.forms import ModelForm, TextInput, Textarea


class HelloForm(ModelForm):
    class Meta:
        model = Hello
        fields = ["froms", 'hello']
        widgets = {
            "froms": TextInput(attrs={
                'class': "form-control",
                'placeholder': "От кого"
            }),
            "hello": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Ваш привет"
            })
        }