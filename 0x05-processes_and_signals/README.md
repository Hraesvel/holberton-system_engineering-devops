# 0x05. Processes and signals


man or help:

* ps
* pgrep
* pkill
* kill
* exit
* trap

## Tasks:

### [what-is-my-pid](0-what-is-my-pid)

Bash script that displays its own PID.

```
$ ./0-what-is-my-pid
4120
$ 
```

### [list_your_processes](1-list_your_processes)

Bash script that displays a list of currently running processes.

Requirements:

* Must show all processes, for all users, including those which might not have a TTY
* Display in a user-oriented format
* Show process hierarchy

```
$ ./1-list_your_processes | head -10
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ksoftirqd/0]
root         4  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/0:0]
root         5  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/0:0H]
root         7  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [rcu_sched]
root         8  0.0  0.0      0     0 ?        S    Feb13   0:03  \_ [rcuos/0]
root         9  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcuob/0]
root        11  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [migration/0]
$ 
```

### [show_your_bash_pid](2-show_your_bash_pid)

Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

* Cannot use `pgrep`
* The third line of your script must be `# shellcheck disable=SC2009`

```
./2-show_your_bash_pid
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_PID
sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep
$ 
```

### [show_your_bash_pid_made_easy](3-show_your_bash_pid_made_easy)

Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

Requirements:

* Cannot use `ps`


### [to_infinity_and_beyond](4-to_infinity_and_beyond)

Bash script that displays To infinity and beyond indefinitely.

Requirements:

* In between each iteration of the loop, add a `sleep 2`

```
$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
^C
$ 
```
Note `ctrl+c` (killed) the Bash script in the example.

### [kill_me_now](5-kill_me_now)

We killed our `4-to_infinity_and_beyond` process using `ctrl+c` in the previous task, there is actually another way to do this.

Write a Bash script that kills `4-to_infinity_and_beyond` process.

Requirements:

* You must use `kill`

**Terminal #0**

```
$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
$ 
```

**Terminal #1**

```
$ ./5-kill_me_now 
$ 
```
I opened 2 terminals in this example, started by running my `4-to_infinity_and_beyond` Bash script in terminal #0 and then moved on terminal #1 to run `5-kill_me_now`. We can then see in terminal #0 that my process has been terminated.

### [kill_me_now_made_easy](6-kill_me_now_made_easy)

Write a Bash script that kills `4-to_infinity_and_beyond` process.

Requirements:

* You cannot use `kill` or `killall`

**Terminal #0**

```
$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
$ 
```

**Terminal #1**

```
$ ./6-kill_me_now_made_easy 
$ 
```

### [highlander](7-highlander)

Write a Bash script that displays:

* `To infinity and beyond` indefinitely
* With a `sleep 2` in between each iteration
* `I am invincible!!!` when receiving a `SIGTERM` signal

copy of your `6-kill_me_now_made_easy` script as `67-kill_me_now_made_easy`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one.

**Terminal #0**

```
$ ./7-highlander
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
^C
$ 
```

**Terminal #1**

```
$ ./67-kill_me_now_made_easy 
$ ./67-kill_me_now_made_easy 
$ ./67-kill_me_now_made_easy
$
```

started `7-highlander` in Terminal #0 and then run `67-kill_me_now_made_easy` in terminal #1, for every iteration we can see `I am invincible!!!` appearing in terminal #0.


### [beheaded_process](8-beheaded_process)

Write a Bash script that kills the process `7-highlander`.

Terminal #0

```
$ ./7-highlander 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Killed
$ 
```

Terminal #1

```
$ ./8-beheaded_process
$
``` 

