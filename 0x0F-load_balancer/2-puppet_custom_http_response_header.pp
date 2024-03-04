# use ha proxy using puppet

exec {'sudo apt-get update':
  provider => shell
}

exec {'sudo apt-get install -y nginx':
  provider => shell
}

exec {'sed -i "/listen 80 default_server;/a add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default':
  provider => shell
}

exec {'sed -i "/listen 80 default_serve;/a rewrite ^/redirect_me https://linkedin.com permanent;" /etc/nginx/sites-available/default':
  provider => shell
}

exec {'sed -i "/listen 80 default_serve;/a rewrite ^/redirect_me https://linkedin.com permanent;" /etc/nginx/sites-available/default':
  provider => shell
}

exec {'sed -i "/listen 80 default_server;/a error_page 404 /notfound_404.html;" /etc/nginx/sites-available/default':
  provider => shell
}

exec {'sudo service nginx restart':
  provider => shell
}
