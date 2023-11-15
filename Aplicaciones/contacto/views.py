from django.shortcuts import render
from .models import Contacto
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
#from django.contrib.auth.decorators import login_required


def contacto(request):
    if request.method == "POST":
        data = request.POST
        tname = request.POST["name"]
        temail = request.POST["email"]
        tphone = request.POST["phone"]
        tmessage = request.POST["message"]
        subject = 'Nueva empresa interesada'
        email_html(subject, data)
        obj_contact = Contacto(name=tname,email=temail,phone=tphone,message=tmessage)
        obj_contact.save()
    return render(request,"pages/contact.html",)
# Create your views here.

def email_html(subject, data):
    html_message = ('<div style-"font-family: sans-serif; text-align:center; border: 1px solld #412378: margin-top: 30px;max-width: 550px;margin: 0 auto:">' +
        '<div style-"background-color: #a90a59; padding:spx;">' +
            '<h1>Contacto nuevo</h1>' +
        '</div>' +
        '<div style-"padding:20px; font-s1ze:16px;">' +
            'Se has registrado como contacto - ' + data['name'] +
            ' con el correo: ' + data['email'] + '.<br>' +
            'Teléfono: ' + str(data['phone']) + '.<br>' +
            'Mensaje: ' + str(data['message']) + '<br>'+
        '</div>' +
    '</div>'
    )
    print(html_message)
    from_email = settings.EMAIL_HOST_USER
    send_mail(
        subject=subject,
        message='',
        html_message=html_message,
        from_email=from_email,
        recipient_list=['24danielcamilo@gmail.com']
    )

