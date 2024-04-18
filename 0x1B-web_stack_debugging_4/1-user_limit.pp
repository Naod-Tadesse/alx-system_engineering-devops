# file desc
exec {
    'replace the limit':
    command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 1500/" /etc/security/limits.conf',
    path    => ['/bin/','/usr/bin/']
}

exec {
    'replace soft limit':
    command => 'sed -i "s/holberton soft nofile 4/holberton hard nofile 1000/" /etc/security/limits.conf',
    path    => ['/bin/','/usr/bin/']
}
