from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import ChatMessage
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

