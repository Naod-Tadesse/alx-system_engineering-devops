# this script installs flask using pip 3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
