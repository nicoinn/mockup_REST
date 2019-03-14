# Ultra simple mock-up REST API

This implements a ultra-simple REST API that will do nothing more than recording any json data sent to it and replying 'ok' to everything.

Endpoints:
- / : replies the data from the latest 20 requests
- /api/sink/ : records any json sent to it and replies `ok`

## What for ?

To live demo that a software stack eventually talks to a REST API that doesn't exist yet.... nothing more, nothing less ;)

## Build the image:

```
docker build . -t rest_mockup
```

## Running:
```
docker run -ti -p 5000:5000 rest_mockup
```

Or, if you want to store the queries in a file locally

```
docker run -ti -p 5000:5000 -v ./some/path/to/a/local/folder/:/data  rest_mockup
```


##Basic Usage:

First, you need to send in some data to the REST api. There are many ways of doing so! See 2 examples below.
Once data has been sent, just access [http://localhost:5000] with you browser to view the last 20 requests received.


### Curl:

```
curl --header "Content-Type: application/json"   --request GET   --data '{"username":"xyz","password":"xyz"}' http://127.0.0.1:5000/api/sink/
```

### Python:
```
import requests
res = requests.post('http://localhost:5000/api/sink/', json={"mytext":"lalala"})
```

## Running - advanced version

It is possible to easily run the mockup REST API using a SSL encryption and a Let's Encrypt SSL certificate. A suitable configuration is given in  ```docker-compose.yml```, it will automagically request the certificate from Let's Encrypt and use Nginx to correctly reverse-proxy the API.


Start by creating a subdomain for the rest api (ex: ```rest.mydomain.io```)

Then copy example override file

```cp docker-compose.yml.override.sample docker-compose.yml.override```

Edit ```docker-compose.yml.override```filling in the correct information, i.e. adapt these line to your specific case:
```
- VIRTUAL_HOST=rest.mydomain.com
- LETSENCRYPT_HOST=rest.mydomain.com
- LETSENCRYPT_EMAIL=me@mydomain.com
```



Save, and then simply run ```docker-compose up -d```  - compose will automatically build and/or download the necessary images and run everything.
