# DeveloperFolio Server

Contact Form API that involves sending Thanking You Mail from the contacting email_id provided.

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



