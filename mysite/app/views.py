from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import Client_update
from django.urls import reverse


def Home(request):
    client = Client_update.objects.all()
    return render(request, "home.html", {"clients": client})


def Book_apt(request, id):
    try:
        client = Client_update.objects.filter(id=id)  #
    except Client_update.DoesNotExist:
        return render(request, "error.html", {"message": "Client not found"})  

    if request.method == "POST":
        global user_email , date , time , purpose_booking
        purpose_booking = request.POST.get("purpose_booking")
        user_email = request.POST.get("user_email")
        date = request.POST.get("date")
        time = request.POST.get("time")

        subject = "Appointment Request"
        from_email = user_email
        recipient_list = [client.get().email]  
        accept_url = request.build_absolute_uri(reverse('accept_appointment', args=[client.get().id]))
        reject_url = request.build_absolute_uri(reverse('reject_appointment', args=[client.get().id]))

        html_message = render_to_string("email.html", {
            "client_name": "{}\t{}".format(client.get().firstname, client.get().lastname),
            "appointment_date": date,
            "appointement_time": time,
            "client_address": client.get().address,
            "client_about": client.get().about,
            "purpose": purpose_booking,
            "user_email": user_email,
            "accept_url": accept_url,
            "reject_url": reject_url,
        })

        send_mail(
            subject=subject,
            message="",  
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message
        )

    return render(request, "book_apt.html", {"data": client})


def accept_appointment(request, id):
    client = get_object_or_404(Client_update, id=id)
    client.status = 'Accepted'  
    client.save()

    messages.success(request, f"Appointment with has been accepted.")

    html_message = render_to_string("congrats.html" , {
        "clients" : client,
        "user_email":user_email,
        "time":time,
        "date":date ,
        "purpose_booking":purpose_booking
    })

    send_mail(
        subject="Appointment has been Confirm",
        message="",
        from_email=client.email,
        recipient_list=[user_email],
        html_message=html_message
    )
    return redirect('/')  


def reject_appointment(request, id):
    client = get_object_or_404(Client_update, id=id)
    client.status = 'Rejected'  
    client.save()

    messages.success(request, f"Appointment with has been rejected.")
    print("rejects")
    return redirect('/')  


def Client_side(request): 
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        photo = request.FILES.get("photo")
        about = request.POST.get("about") 
        address = request.POST.get("address")
        exp_years = request.POST.get("exp_years")

        dataentry = Client_update(
            firstname=firstname, 
            address=address,
            lastname=lastname,
            email=email, 
            photo=photo, 
            about=about,
            exp_years=exp_years
            )     
        dataentry.save()
    return render(request, "clientside.html")

def all_appointement(request):
    client = Client_update.objects.all()
    return render(request , "all_appointement.html" , {"clients" : client})

def about(request):
    return render(request , "about.html")