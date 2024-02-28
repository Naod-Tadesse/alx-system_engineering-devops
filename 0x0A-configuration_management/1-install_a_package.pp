# this script installs flask using pip 3

exec { 'pip3 install flask==2.1.0':
  provider => shell
}
