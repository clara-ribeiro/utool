from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django import utils

class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user.nome = data["nome"]
        user.sobrenome = data["sobrenome"]
        user.email = data["email"]
        user.cpf = data['cpf']
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        user.save()
        return user