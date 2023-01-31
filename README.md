# graduation-lw

```bash
# Generate cert
docker-compose -f docker-compose.cert.yml up certbot

# Start application
sudo docker-compose up -d --build
```

## How to cert nginx

<https://blog.jarrousse.org/2022/04/09/an-elegant-way-to-use-docker-compose-to-obtain-and-renew-a-lets-encrypt-ssl-certificate-with-certbot-and-configure-the-nginx-service-to-use-it/>
