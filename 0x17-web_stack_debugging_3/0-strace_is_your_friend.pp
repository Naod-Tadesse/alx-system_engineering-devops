# fix bug in wordpress site
$settings = 'www/html/wp-settings.php'

exec { 'wordpess site fix':
  command => 'sudo sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin'
}
