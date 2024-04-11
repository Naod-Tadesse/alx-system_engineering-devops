# fix bug in wordpress site

exec { 'fix the type phpp->php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin'
}
