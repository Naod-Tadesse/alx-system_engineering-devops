# use puppet to set up header

exec {'sudo apt-get -y update':
  provider => shell
}

exec {'sudo apt-get -y install nginx':
  provider => shell
}

exec {'sudo sed -i "/server {/a add_header X-Served-By \$hostname;" /etc/nginx/sites-enabled/default':
  provider => shell
}

exec {'sudo service nginx restart':
  provider => shell
}
