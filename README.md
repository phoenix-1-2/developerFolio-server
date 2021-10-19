# DeveloperFolio Server

Contact Form API that involves sending Thanking You Mail from the contacting email_id provided.

## Django Sending Email 
<br />

### Option 1

```from django.core.mail import send_mail

def send_mail_django(user):
    subject = f"Hey Nikhil,{user['name']} Messaged You!!"
    from_mail = settings.EMAIL_HOST_USER
    to_mail = [
        "bhasin.nikhil.12@gmail.com",
        "nikhil.bhasin124@gmail.com",
    ]
    message = f"Hey Nikhil,\n{user['name']} has messaged you.\n\n'{user['message']}'\n\nReply ASAP.\nRegards,\nNikhil"
    send_mail(subject, message, from_mail, to_mail)
```
<br />
### Option 2

```from django.core.mail import EmailMultiAlternatives

def send_mail_django(user):
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
```

<br />
### cURL

```curl --location --request POST 'https://developerfolio-server.herokuapp.com/apis/contact' \
--form 'name="Rahul"' \
--form 'email="example@example.com"' \
--form 'message="Hey,There!!"'

```
<br />
### Javascript

```var formdata = new FormData();
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

<br />
### Python 

```import requests

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
