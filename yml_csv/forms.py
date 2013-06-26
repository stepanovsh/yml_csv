# -*- coding: utf-8 -*-
from django import forms
from time import time

class FormImportXML(forms.Form):
    file_yml = forms.FileField(label="Выберите YML фаил")


