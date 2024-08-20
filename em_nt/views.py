from django.shortcuts import render, redirect
from .models import Signals
from django.http import HttpResponse
from django.core.mail import send_mail
from datetime import datetime, timedelta

def sg(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("message")

        last_submission = (
            Signals.objects.filter(email=email).order_by("-submitted_at").first()
        )

        if last_submission and datetime.now() - last_submission.submitted_at.replace(
            tzinfo=None
        ) < timedelta(hours=24):

            # Send an email to notify that a submission was already made within 24 hours
            send_mail(
                "Enquiry Form Submission",
                f"""
                You have received a new enquiry submission.

                Name: {name}
                Email: {email}
                Mobile: {mobile}
                Message: {message}

                Please respond to the enquiry accordingly.
                """,
                "julasarfraj@gmail.com",  
                [email],  
                fail_silently=False,
            )
            return HttpResponse(
                "You have already submitted an enquiry. Please try again after 24 hours."
            )

        student = Signals(name=name, email=email, mobile=mobile, message=message)
        student.save()

        return HttpResponse("Data added successfully.")

    return render(request, "index.html")

