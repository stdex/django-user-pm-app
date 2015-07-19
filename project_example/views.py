from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as contrib_login, logout as contrib_logout
from django.template import Context, loader, RequestContext, Template
from django.template import loader
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.db.models import Q

def root(request, **kwargs):
    return render(request,'base.html', locals())