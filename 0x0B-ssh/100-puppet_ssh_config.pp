# this modifies the config
file {'/etc/ssh/ssh_config':
  ensure  => present,
  content => "
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
  "
}
