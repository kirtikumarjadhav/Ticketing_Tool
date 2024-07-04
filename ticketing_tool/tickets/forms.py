from django import forms
from .models import Ticket, Comment
from allauth.account.forms import SignupForm
from allauth.account.forms import SignupForm
from django import forms
from .models import User

class CustomSignupForm(SignupForm):
    is_customer = forms.BooleanField(required=False, label="Sign up as Customer")
    is_engineer = forms.BooleanField(required=False, label="Sign up as Engineer")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.is_customer = self.cleaned_data['is_customer']
        user.is_engineer = self.cleaned_data['is_engineer']
        user.save()
        return user


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status', 'assigned_engineer']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

