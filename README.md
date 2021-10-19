# DeveloperFolio Server

Contact Form API that involves sending Thanking You Mail from the contacting email_id provided.

## Django Sending Email 
(https://docs.djangoproject.com/en/3.2/topics/email/) \\

settings.py

```
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "email@email.com"
EMAIL_HOST_PASSWORD = "password"
```

### Using send_mail

```
from django.core.mail import send_mail
def send_mail_django():
    subject = f"Hey,Nikhil Here !!"
    from_mail = settings.EMAIL_HOST_USER
    to_mail = [
     "email@email.com"
    ]
    message = f"Hey,Nikhil Here !!"
    send_mail(subject, message, from_mail, to_mail)
```

### Using EmailMultiAlternatives ( Best for Email Templates)
```
from django.core.mail import EmailMultiAlternatives

def send_mail_django():
    subject = f"Hey,Nikhil Here !!"
    from_mail = settings.EMAIL_HOST_USER
    to_mail = [
       "email@email.com",
    ]
    text_content = ""
    html_content = "<h1>Thank You !!</h1>"
    msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
```

### cURL

```
curl --location --request POST 'https://developerfolio-server.herokuapp.com/apis/contact' \
--form 'name="Rahul"' \
--form 'email="example@example.com"' \
--form 'message="Hey,There!!"'
```

### Javascript

```
var formdata = new FormData();
formdata.append("name", "Rahul");
formdata.append("email", "example@example.com");
formdata.append("message", "Hey,There!!");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("https://developerfolio-server.herokuapp.com/apis/contact", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

### Python 

```
import requests

url = "https://developerfolio-server.herokuapp.com/apis/contact"

payload={'name': 'Rahul',
'email': 'example@example.com',
'message': 'Hey,There!!'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```
