# this file will create a file

# check is user and group is present
user { 'www-data':
  ensure => 'present',
  gid    => 'www-data'
}

# create a file
file { '/tmp/holberton':
    ensure  => 'present',
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
