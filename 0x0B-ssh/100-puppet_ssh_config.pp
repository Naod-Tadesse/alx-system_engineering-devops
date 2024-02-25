# this modifies the config
file {'/home/ssh_conf':
  ensure  => present,
  content => "
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
  "
}
