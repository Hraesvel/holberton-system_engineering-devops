include stdlib
file {'/var/www/html':
  ensure => present,
}-> file_line { 'fix a line in wp-settings.php':
  path               => '/var/www/html/wp-settings.php',
  line               => '/class-wp-locale.php',
  match              => '/class-wp-locale.phpp',
  append_on_no_match => false,
}
