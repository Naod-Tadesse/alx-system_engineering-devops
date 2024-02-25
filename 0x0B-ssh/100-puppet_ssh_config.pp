# this modifies the config
file {'/home/ssh_config':
  ensure  => present,
  content => "
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
  "
}
