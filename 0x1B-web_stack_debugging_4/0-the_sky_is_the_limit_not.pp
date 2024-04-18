# Define the sed command to change the file des
file { '/etc/default/nginx':
  ensure  => file,
  content => template('module_name/nginx_config.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/default/nginx'],
}
