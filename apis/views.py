from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from datetime import datetime, timedelta
import requests
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


client = settings.CLIENT


def replace(html_content, search_string, replace_string):
    index = html_content.find(search_string)
    html_content = (
        html_content[:index]
        + replace_string
        + html_content[index + len(search_string) :]
    )
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
    html_content = requests.get(
        "https://res.cloudinary.com/phoenix-redstone-04/raw/upload/v1633628764/contact_images/beefree-j4oeb9xlex_voljzf_ymjdro.html"
    ).text
    html_content = replace_from_template(html_content, user["name"])
    msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@api_view(["POST"])
def contact(request):
    name = request.data.get("name")
    email = request.data.get("email")
    message = request.data.get("message")
    date = datetime.now()

    user = {"name": name, "email": email, "message": message, "date": date}

    db = client["Contact_Information"]
    collection = db["Contact_Information"]

    old_user = collection.find_one({"name": name, "email": email})
    if old_user and (old_user["date"] < (datetime.now() + timedelta(days=7))):
        return JsonResponse(
            {"message": "Already has submitted query that is not answered"}, status=307
        )
    collection.insert_one(user)
    send_thankyou_mail(user)
    response = {"message": "Success"}
    return JsonResponse(response, status=201)
