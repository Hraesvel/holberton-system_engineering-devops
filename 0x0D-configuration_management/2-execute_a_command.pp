# This manifest will kill a process name killmenow
exec { 'pkill -f killmenow':
}
