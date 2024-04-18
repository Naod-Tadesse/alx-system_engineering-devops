# Define the sed command to change the file descriptors in the nginx default configuration file
exec { 'change_nginx_file_descriptors':
  command     => '/usr/bin/env sed -i s/15/4096/ /etc/default/nginx',
  path        => ['/usr/bin', '/usr/sbin', '/bin'],
  refreshonly => true, # Only run when notified
}

# Define a service resource to restart the nginx service when necessary
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['change_nginx_file_descriptors'], # Subscribe to the exec resource
}

