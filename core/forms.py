from django import forms
from django.core.mail import send_mail
from django.conf import settings

from core.mail import send_mail_template

class Contact(forms.Form):
    name = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail")
    telefone = forms.CharField(label="Telefone")
    subject = forms.CharField(label="Assunto")
    message = forms.CharField(label="Mensagem", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'styled-input'
        self.fields['email'].widget.attrs['class'] = 'styled-input'
        self.fields['telefone'].widget.attrs['class'] = 'styled-input'
        self.fields['subject'].widget.attrs['class'] = 'styled-input'        
        self.fields['message'].widget.attrs['class'] = 'styled-input textarea-grid'

    def send_mail(self):
        subject = 'Contato'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'telefone': self.cleaned_data['telefone'],
            'subject': self.cleaned_data['subject'],
            'message': self.cleaned_data['message'],
        }
        template_name = 'contact_email.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])
