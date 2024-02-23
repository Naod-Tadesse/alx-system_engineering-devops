exec {'killtheprocess':
  command => '/usr/bin/pkill -f killmenow'
}
