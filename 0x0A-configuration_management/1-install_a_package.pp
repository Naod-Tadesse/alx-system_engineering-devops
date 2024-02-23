# this script installs flask using pip 3

exec { 'installflask':
  command => '/usr/bin/pip3 install flask==2.1.0',
}
