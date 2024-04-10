$edit = 'www/html/wp-settings.php'
exec { 'phpp->php':
  command => 'sed -i s/phpp/php/g /var/${edit}',
  path    => '/bin'
}
