# Define the sed command to change the file des
exec { 'update_nginx_config':
  command     => '/usr/bin/sed -i s/15/4096/ /etc/default/nginx',
  refreshonly => true,
  notify      => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/bin/env service nginx restart',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}

