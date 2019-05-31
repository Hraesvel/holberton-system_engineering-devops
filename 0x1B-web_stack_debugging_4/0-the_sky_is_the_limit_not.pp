# this file will increase the ULIMIT so taht workers can handel more open files.
file { '/etc/default/nginx':
  ensure => present,
} -> exec { 'increase ULIMIT':
  path    => '/bin/',
  command => "sed -i 's/15/1024/g' /etc/default/nginx"
}
