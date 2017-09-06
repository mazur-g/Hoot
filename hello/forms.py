from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import (FormActions)

class GeoMessageForm(forms.Form):

    def __init__(self):
        self._message = forms.CharField(label='message', max_length=150)

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
