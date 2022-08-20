# upstream  django_app{
#     server app:8000;
# }

# server {
#     listen 80;

#     location / {
#         proxy_pass http://django;
#     }

#     location /static/{
#         alias ./static/;
#     }
    
# }
server {
    listen ${LISTEN_PORT};

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}