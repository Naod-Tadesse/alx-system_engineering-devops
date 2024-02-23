# this script kills process

exec {'killtheprocess':
  command => '/usr/bin/pkill -f killmenow'
}
