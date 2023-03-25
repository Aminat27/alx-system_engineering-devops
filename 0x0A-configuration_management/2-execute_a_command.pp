# kills a process named kiilmenow

exec { 'pkill':
  command  => 'pkill  killmenow',
  provider => 'shell',
}
