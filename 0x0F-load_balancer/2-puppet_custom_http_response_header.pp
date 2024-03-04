# use ha proxy using puppet

exec {'sudo apt-get -y update':
  provider => shell
}

exec {'sudo apt-get -y install nginx':
  provider => shell
}

exec {'sudo sed -i "/listen 80 default_server;/a add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default':
  provider => shell
}

exec {'sudo service nginx restart':
  provider => shell
}
