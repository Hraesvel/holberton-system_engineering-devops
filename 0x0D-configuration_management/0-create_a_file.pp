user { 'www-data':
  ensure => 'present',
  gid    => 'www-data'
}

file { '/tmp/holberton':
    ensure  => 'present',
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
