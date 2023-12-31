from django.views.generic import TemplateView
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


def send_email(request):
    name = request.POST.get("name")
    number = request.POST.get("number")
    message = request.POST.get("message")

    if name and number and message:
        try:
        # Send the email
            send_mail(
                "Новый заказ букета!",
                f"Новый заказ\nИмя: {name}\nНомер телефона: {number}\nСообщение: {message}", settings.EMAIL_HOST_USER,
                ["lenayar67@gmail.com"],  # List of recipient email addresses
                fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        # Redirect the user after successful submission (you can customize the URL)
        return HttpResponseRedirect("/thanks/")
    else:
    # In reality we'd use a form class
    # to get proper validation errors.
        return HttpResponse("Убедитесь что все поля заполнены верно.")


class HomePageView(TemplateView):
    template_name = "home.html"


class ThanksPageView(TemplateView):
    template_name = "thanks.html"
