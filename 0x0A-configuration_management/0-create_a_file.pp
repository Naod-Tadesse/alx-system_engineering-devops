# this script creates file school in tmp folder

file { '/tmp/school':
  content => 'I love Puppet',
  owner   => 'www-data',
  mode    => '0744',
  group   => 'www-data'
}
