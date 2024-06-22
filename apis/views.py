from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from datetime import datetime, timedelta
import requests
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from profanity import profanity_list
from multiprocessing import Pool

EMAIL_LINK = "https://res.cloudinary.com/phoenix-redstone-04/raw/upload/v1633666528/contact_images/email_yydewd.html"

client = settings.CLIENT


def replace(html_content, search_string, replace_string):
    index = html_content.find(search_string)
    html_content = html_content[:index] + replace_string + html_content[index + len(search_string) :]
    return html_content


def replace_from_template(html_content, name):
    html_content = replace(html_content, "[Name]", f"{name}")
    return html_content


def send_thankyou_mail(user):
    subject = f"Hey {user['name']}, Nikhil Here !!"
    from_mail = settings.EMAIL_HOST_USER
    to_mail = [
        user["email"],
    ]
    text_content = ""
    html_content = requests.get(EMAIL_LINK).text
    html_content = replace_from_template(html_content, user["name"])
    msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_mail_to_me(user):
    subject = f"Hey Nikhil,{user['name']} Messaged You!!"
    from_mail = settings.EMAIL_HOST_USER
    to_mail = [
        "bhasin.nikhil.12@gmail.com",
    ]
    message = f"Hey,\n{user['name']} has messaged you.\n\n'{user['message']}'\n\nReply ASAP.\nRegards,\nNikhil"
    send_mail(subject, message, from_mail, to_mail)


@api_view(["POST"])
def contact(request):
    try:
        name = request.data.get("name")
        email = request.data.get("email")
        message = request.data.get("message")
        date = datetime.now()

        if any(word in profanity_list for word in message.lower().split()) or any(
            word in profanity_list for word in name.lower().split()
        ):
            return JsonResponse({"message": "Profanity language not allowed"}, status=400)
        user = {"name": name, "email": email, "message": message, "date": date}

        db = client["Contact_Information"]
        collection = db["Contact_Information"]

        old_user = collection.find_one({"name": name, "email": email})
        if old_user and (old_user["date"] < (datetime.now() + timedelta(days=7))):
            return JsonResponse(
                {"message": "Already has submitted query that is not answered"},
                status=307,
            )
        collection.insert_one(user)
        pool = Pool()
        pool.apply_async(send_thankyou_mail, args=(user,))
        pool.apply_async(send_mail_to_me, args=(user,))
        response = {"message": "Success"}
        return JsonResponse(response, status=201)

    except Exception:
        response = {"message": "Some Error Occured"}
        return JsonResponse(response, status=500)
