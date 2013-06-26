# -*- coding: utf-8 -*-
from yml_csv.forms import FormImportXML
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from yml_csv.settings import MEDIA_ROOT
from time import time

def first_pars_file(request_file):
    name = '%s/%s_%s'%(MEDIA_ROOT, str(time()).replace('.','_'), 'yml_tm.xml')
    tmp_file = open(name, 'wb+')
    for chunk in request_file.chunks():
        tmp_file.write(chunk)
    tmp_file.close()
    return name

def import_yml(request):
    if request.POST:
        form = FormImportXML(request.POST, request.FILES)
        if form.is_valid():
            first_pars_file(request.FILES['file_yml'])

        else:
            form = FormImportXML(request.POST, request.FILES)
    else:
        form = FormImportXML

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response("upload.html", args)




