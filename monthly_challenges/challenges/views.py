from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february":  "Work for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Workout every day",
    "may": "Go on a walk for 10 mins a day",
    "june": "Use the treadmil for an hour a week",
    "july": "Learn React",
    "august": "Apply for internhip",
    "september": "Practice for interviews",
    "october": "Explore the world",
    "november": "Go to interview",
    "december": "Go home for christmas"
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenges/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
