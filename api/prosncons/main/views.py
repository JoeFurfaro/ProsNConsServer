from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from main.models import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
import uuid

@api_view(['POST'])
def view_post(request):
    try:
        print(request.data)
        title = request.data["title"]
        author = request.data["author"]
        pros = request.data["pros"].split("|||||")
        cons = request.data["cons"].split("|||||")

        pros = [PCPro.objects.create(text=str(pro)) for pro in pros]
        cons = [PCCon.objects.create(text=str(con)) for con in cons]

        new_id = uuid.uuid4()
        new_post = PCPost.objects.create(title=title, author=author, id=str(new_id))
        new_post.pros.add(*pros)
        new_post.cons.add(*cons)
        new_post.save()

        resp = JsonResponse({"post_id": str(new_id) }, status="200")
        resp["Access-Control-Allow-Origin"] = "*"
        return resp
    except Exception as e:
        print(e)
    resp = JsonResponse({}, status="400")
    resp["Access-Control-Allow-Origin"] = "*"
    return resp

@api_view(['GET'])
def view_get(request):
    try:
        id = request.GET["id"]
        post = PCPost.objects.filter(id=id)
        if post:
            resp = JsonResponse(post[0].export(), status="200")
            resp["Access-Control-Allow-Origin"] = "*"
            return resp
        resp = JsonResponse({}, status="404")
        resp["Access-Control-Allow-Origin"] = "*"
        return resp

    except Exception as e:
        print(e)
    resp = JsonResponse({}, status="400")
    resp["Access-Control-Allow-Origin"] = "*"
    return resp