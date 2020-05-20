from django import forms


class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('pretty.css',)
        }
        js = ('animations.js', 'actions.js')


class RegisterForm(forms.Form):
    name = forms.CharField(label='Your name ', max_length=100, initial='abeke')
    email = forms.EmailField(label='Your email ', max_length=200, initial='abekedevelops@gmail.com')
    password = forms.CharField(label='Your password ', max_length=100, initial=123)
    confirm_password = forms.CharField(label='Confirm Your password ', max_length=100, initial=123)
    # photo = forms.FileField()


