# create a file in tmp/school

file { '/tmp/school':
  ensure  => present,
  content => "I love Puppet\n",
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}

