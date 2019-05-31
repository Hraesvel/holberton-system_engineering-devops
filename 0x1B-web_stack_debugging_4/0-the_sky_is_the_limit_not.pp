# I'll fix your code!
file { '/etc/default/nginx':
  ensure => present,
} -> exec { 'increase fs.open':
  path    => '/bin/',
  command => "sed -i 's/15/1024/g' /etc/default/nginx"
}
