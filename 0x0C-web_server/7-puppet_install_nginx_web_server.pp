# this puppet file installs nginx

exec{'sudo apt-get -y update':
  provider => shell,
}

exec{'sudo apt-get -y install nginx':
  provider => shell
}

exec {'echo "Hello World!" | sudo tee /var/www/html/index.html > /dev/null':
  provider => shell
}

exec {'sed -i "67i rewrite ^/redirect_me https://www.twitter.com permanent;" /etc/nginx/sites-available/default':
  provider => shell
}

exec {'echo "Ceci n\'est pas une page" | sudo tee /var/www/html/notfound_404.html':
  provider => shell
}

exec {'sed -i "67i error_page 404 /notfound_404.html;" /etc/nginx/sites-available/default':
  provider => shell
}

exec {'sudo service nginx restart':
  provider => shell
}
