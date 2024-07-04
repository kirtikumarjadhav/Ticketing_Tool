from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def get_user_model(self):
        from django.contrib.auth import get_user_model
        return get_user_model()