#Creates a file with a content

file { '/tmp/school' :
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'i love Puppet'
  }
