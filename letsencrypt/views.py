from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_GET
import os

def lets_encrypt(request, cid):
    try:
        ch_default = os.environ['LE_CHALLENGES']
    except:
        ch_default = ".-nKGkamsfmmJUr8dFAFKOPtuyAedMginKBLHr-LyX0s"
    return HttpResponse(cid + ch_default, content_type="text/plain")
