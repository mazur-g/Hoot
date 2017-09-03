from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import(FormActions)

class RegistrationForm(forms.Form):
	username = forms.CharField(label='Username',max_length=30)
	email = forms.EmailField(label='Email')
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
	password2 = forms.CharField(label='Password(Again)', widget=forms.PasswordInput())
	image = forms.ImageField(label='Your photo(optional)',required=False)

	helper=FormHelper()
	helper.form_method='POST'
	helper.form_class= 'form-horizontal'
	helper.label_class= 'col-lg-4'
	helper.field_class= 'col-lg-4'

	helper.layout = Layout(
		Field('username', css_class='input-sm'),
		Field('email', css_class= 'input-sm'),
		Field('password1', css_class='input-sm'),
		Field('password2', css_class='input-sm'),
		Field('image', css_class='input-sm'),
		FormActions(Submit('register','Register',css_class='btn-primary')))



	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1 == password2:
				return password2
			raise forms.ValidationError('Passwords do not match.')

	def clean_username(self):
		username=self.cleaned_data['username']
		if not re.search(r'^\w+$',username):
			raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
		try:
			User.objects.get(username=username)

		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('Username is already taken.')	


class SearchForm(forms.Form):
	name = forms.CharField(label='Username',max_length=30)
	