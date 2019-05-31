# I'll fix your code!
file { '/etc/default/nginx':
  ensure => present,
} -> exec { 'increase fs.open':
  path    => '/bin/',
  command => "sed -i 's/4/20/g' /etc/default/nginx"
}
