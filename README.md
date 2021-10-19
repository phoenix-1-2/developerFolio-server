# DeveloperFolio Server

Contact Form API that involves sending Thanking You Mail from the contacting email_id provided.

### Curl

```
curl --location --request POST 'https://developerfolio-server.herokuapp.com/apis/contact' \
--form 'name="Rahul"' \
--form 'email="fake-api@nikhil124738838o397r9.com"' \
--form 'message="Hey"'

```

### Javascript

```
var formdata = new FormData();
formdata.append("name", "Rahul");
formdata.append("email", "fake-api@nikhil124738838o397r9.com");
formdata.append("message", "Hey");

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
