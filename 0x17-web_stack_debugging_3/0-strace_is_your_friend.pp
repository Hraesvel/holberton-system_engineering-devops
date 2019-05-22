# this does something
file {'/var/www/html/wp-settings.php':
  ensure => present,
}-> exec { 'fix a line in wp-settings.php':
  path    => '/usr/local/bin/:/bin/',
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' \
  /var/www/html/wp-settings.php",
}
