from django import  forms
from app1.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             from django import  forms
from app1.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'