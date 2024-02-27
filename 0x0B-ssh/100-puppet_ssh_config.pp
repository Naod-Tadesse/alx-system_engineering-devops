# config file for ssh config file

file_line { 'remove password':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	PasswordAuthentication no',
  replace => true
}

file_line { 'for publickey':
  ensure  =>  present,
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '	IdentityFile ~/.ssh/school',
  replace => true
}
