from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import BotMessage
from openai import OpenAI
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

OpenAI.api_key = settings.OPENAI_API_KEY
client = OpenAI()

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        body = json.loads(request.body)
        user_message = body.get("message")

        response = client.completions.create(
            model="gpt-3.5-turbo",
            prompt=[{"role": "user", "content": user_message}]
        )

        ai_message = response['choices'][0]['message']['content']

        BotMessage.objects.create(
            user_message = user_message,
            ai_response = ai_message
        )

        return JsonResponse({"response": ai_message}, status = 200)
    
    else: 
        return JsonResponse({"error": "POST required"}, status = 405)

@csrf_exempt
def test_view(request):
    user_message = None
    ai_response = None

    if request.method == "POST":
        user_message = request.POST.get("message")

        response = client.completions.create(
            model = "gpt-4o",
            prompt = [{"role": "user", "content": user_message}]
        )

        ai_message = response['choices'][0]['message']['content']

        BotMessage.objects.create(
            user_message = user_message,
            ai_response = ai_message,
        )

    return render(request, "JimBot/bottesting.html", {
        "user_message": user_message,
        "ai_response": ai_response,
    })