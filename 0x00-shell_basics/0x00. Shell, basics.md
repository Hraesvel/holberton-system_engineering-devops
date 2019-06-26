# 0x00. Shell, basics

**Table Of Context**
- [0. Where am I?](#0-Where-am-I?)
- [1. What’s in there?](#1-What’s-in-there?)
- [2. There is no place like home](#2-There-is-no-place-like-home)
- [3. The long format](#3-The-long-format)
- [4. Hidden files](#4-Hidden-files)
- [5. I love numbers](#5-I-love-numbers)
- [6. Welcome holberton](#6-Welcome-holberton)
- [7. Betty in Holberton](#7-Betty-in-Holberton)
- [8. Bye bye Betty](#8-Bye-bye-Betty)
- [9. Bye bye Holberton](#9-Bye-bye-Holberton)
- [10. Back to the future](#10-Back-to-the-future)
- [11. Lists](#11-Lists)
- [12. File type](#12-File-type)
- [13. We are symbols, and inhabit symbols](#13-We-are-symbols,-and-inhabit-symbols)
- [14. Copy HTML files](#14-Copy-HTML-files)
- [15. Let’s move](#15-Let’s-move)
- [16. Clean Emacs](#16-Clean-Emacs)
- [17. Tree](#17-Tree)
- [18. Life is a series of commas, not periods](#18-Life-is-a-series-of-commas,-not-periods)
- [19. File type: Holberton](#19-File-type:-Holberton)

## Tasks

### 0. Where am I?

File: **[0-current_working_directory](0-current_working_directory)**

This script will display the absolute path of the current work directory


<pre><code>$ ./0-current_working_directory
/Users/holbertonschool/holbertonschool-sysadmin_devops/0x00-shell_basics
$
</code></pre>

*[top](#0x00-Shell,-basics)*

---


### 1. What’s in there?
File: **[1-listit](1-listit)**

This script will display the contents of the current directory


<pre><code>$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop Downloads   Library Music Public
$
</code></pre>

*[top](#0x00-Shell,-basics)*

---


### 2. There is no place like home
File: **[2-bring_me_home](2-bring_me_home)**

script will change the working directory to the user's home directory.


```
martin@ubuntu:/tmp$ pwd
/tmp
martin@ubuntu:/tmp$ echo $HOME
/home/julien
martin@ubuntu:/tmp$ source ./2-bring_me_home
martin@ubuntu:~$ pwd
/home/julien
martin@ubuntu:~$

```



*[top](#0x00-Shell,-basics)*

---


### 3. The long format
File: **[3-listfiles](3-listfiles)**

script that will display the current contents of a directory in long format.


```
$ ./3-listfiles
total 32
martin@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
martin@ 1 sylvain staff 19 Jan 25 00:23 1-listit
martin@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
martin@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
$

```



*[top](#0x00-Shell,-basics)*

---


### 4. Hidden files
File: **[4-listmorefiles](4-listmorefiles)**

script that will display all file including hidden ones in the current directory.


```
$ ./4-listmorefiles
total 32
martin@ 6 sylvain staff 204 Jan 25 00:29 .
martin@ 43 sylvain staff 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
$

```



*[top](#0x00-Shell,-basics)*

---


### 5. I love numbers
File: **[5-listfilesdigitonly](5-listfilesdigitonly)**

Displays the current directory contents. with the following.

- Long format
- with user and group numerical IDs
- Hidden file are included


```
$ ./5-listfilesdigitonly
total 32
martin@ 6 501 20 204 Jan 25 00:29 .
martin@ 43 501 20 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
-rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
$

```



*[top](#0x00-Shell,-basics)*

---


### 6. Welcome holberton
File: **[6-firstdirectory](6-firstdirectory)**

This script will create a new directory in `/tmp/` named `holberton`


<pre><code>$ ./6-firstdirectory
$ file /tmp/holberton/
/tmp/holberton/: directory
$
</code></pre>

*[top](#0x00-Shell,-basics)*

---


### 7. Betty in Holberton
File: **[7-movethatfile](7-movethatfile)**

this script will move a file called `betty` from `/tmp` and move it into `/tmp/holberton`


<pre><code>$ ./7-movethatfile
$ ls /tmp/holberton/
betty
$
</code></pre>

*[top](#0x00-Shell,-basics)*

---


### 8. Bye bye Betty
File: **[8-firstdelete](8-firstdelete)**

This script will delete the file called `betty` from `/tmp/holberton`


<pre><code>$ ./8-firstdelete
$ ls /tmp/holberton/
$
</code></pre>

*[top](#0x00-Shell,-basics)*

---


### 9. Bye bye Holberton
File: **[9-firstdirdeletion](9-firstdirdeletion)**

This script will delete the directory called `holberton` from `/tmp`


<pre><code>$ ./9-firstdirdeletion
$ file /tmp/holberton
/tmp/holberton: cannot open `/tmp/holberton' (No such file or directory)
$
</code></pre>

*[top](#0x00-Shell,-basics)*

---

### 10. Back to the future

File: **[10-back](10-back)**

This script will change the directory to the previous on.


```
martin@ubuntu:/tmp$ pwd
/tmp
martin@ubuntu:/tmp$ cd /var
martin@ubuntu:/var$ pwd
/var
martin@ubuntu:/var$ source ./10-back
/tmp
martin@ubuntu:/tmp$ pwd
/tmp

```



*[top](#0x00-Shell,-basics)*

---

### 11. Lists

This script will list all file including hidden ones in long format in the current directory, and the its parent directory and the `/boot` directory in this order.

File: **[11-lists](11-lists)**




*[top](#0x00-Shell,-basics)*

---


### 12. File type
File: **[12-file_type](12-file_type)**

this script will display the file type of a file called `iamafile`


<pre><code>ubuntu@ip-172-31-63-244:~$ ./12-file_type
/tmp/iamafile: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped
</code></pre>

*[top](#0x00-Shell,-basics)*

---


### 13. We are symbols, and inhabit symbols
File: **[13-symbolic_link](13-symbolic_link)**

This script will create a symbolic link for `/bin/ls`  as  `__ls__` in the current directory.


```
martin@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
martin@ip-172-31-63-244:/tmp/sym$./13-symbolic_link
martin@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls

```



*[top](#0x00-Shell,-basics)*

---

### 14. Copy HTML files

File: **[14-copy_html](14-copy_html)**

This script will copy all file with the extension `.html` to the parent directory of the current.




*[top](#0x00-Shell,-basics)*

---


### 15. Let’s move
File: **[15-lets_move](15-lets_move)**

This script will copy all file that begin with an uppercase letter to the directory `/tmp/u`


```
martin@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 Holberton
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 Notrebloh
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
martin@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
martin@ip-172-31-63-244:/tmp/sym$ ./15-lets_move
martin@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
martin@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 Holberton
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 Notrebloh

```



*[top](#0x00-Shell,-basics)*

---


### 16. Clean Emacs
File: **[16-clean_emacs](16-clean_emacs)**

This script will delete all emacs tmp --those prefixed with `~` -- files from the current directory


```
martin@ip-172-31-63-244:/tmp/sym$ ls
main.c  main.c~  Makefile~
martin@ip-172-31-63-244:/tmp/sym$ ./16-clean_emacs
martin@ip-172-31-63-244:/tmp/emacs$ ls
main.c
martin@ip-172-31-63-244:/tmp/emacs$

```



*[top](#0x00-Shell,-basics)*

---


### 17. Tree
File: **[17-tree](17-tree)**

this script will create directories `welcome/`, `welcome/to/` and `welcome/to/holberton` in the current directory.


```
martin@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 44 Sep 20 12:09 17-tree
martin@ubuntu:/tmp/h$ wc -l 17-tree
2 17-tree
martin@ubuntu:/tmp/h$ head -1 17-tree
#!/bin/bash
martin@ubuntu:/tmp/h$ tr -cd ' ' < 17-tree | wc -c # you do not have to understand this yet, but the result should be 2, 1 or 0
2
martin@ubuntu:/tmp/h$ ./17-tree
martin@ubuntu:/tmp/h$ ls
17-tree  welcome
martin@ubuntu:/tmp/h$ ls welcome/
to
martin@ubuntu:/tmp/h$ ls -l welcome/to
total 4
drwxrwxr-x 2 julien julien 4096 Sep 20 12:11 holberton
martin@ubuntu:/tmp/h$

```



*[top](#0x00-Shell,-basics)*

---


### 18. Life is a series of commas, not periods
File: **[18-commas](18-commas)**

this script will list all files and directorys in the current directory separated by a commas (`,`).


```
martin@ip-172-31-63-244:~/holbertonschool$ ls -a

.  ..  0-commas  0-commas-checks  1-empty_casks  2-gifs  3-directories  4-zeros  5-rot13  6-odd  7-sort_rot13  Makefile  quote  .test  test_dir  test.var

martin@ip-172-31-63-244:~/holbertonschool$ ./18-commas

./, ../, 0-commas, 0-commas-checks/, 1-empty_casks, 2-gifs, 3-directories, 4-zeros, 5-rot13, 6-odd, 7-sort_rot13, Makefile, quote, .test, test_dir/, test.var

martin@ip-172-31-63-244:~/holbertonschool$

```



*[top](#0x00-Shell,-basics)*

---


### 19. File type: Holberton
File: **[holberton.mgc](holberton.mgc)**

Created a magic file `holberton.mgc` 


```
martin@ip-172-31-63-244:/tmp/magic$ cp /bin/ls .
martin@ip-172-31-63-244:/tmp/magic$ ls -la
total 268
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 02:44 .
drwxrwxrwt 11 root   root   139264 Sep 20 02:44 ..
-rw-r--r--  1 ubuntu ubuntu    496 Sep 20 02:42 holberton.mgc
-rwxr-xr-x  1 ubuntu ubuntu 110080 Sep 20 02:43 ls
-rw-rw-r--  1 ubuntu ubuntu     50 Sep 20 02:06 thisisanholbertonfile
-rw-rw-r--  1 ubuntu ubuntu     30 Sep 20 02:16 thisisatextfile
martin@ip-172-31-63-244:/tmp/magic$ file --mime-type -m holberton.mgc *
holberton.mgc:         application/octet-stream
ls:                    application/octet-stream
thisisanholbertonfile: Holberton
thisisatextfile:       text/plain
martin@ip-172-31-63-244:/tmp/magic$ file -m holberton.mgc *
holberton.mgc:         data
ls:                    data
thisisanholbertonfile: Holberton data
thisisatextfile:       ASCII text
martin@ip-172-31-63-244:/tmp/magic$

```



*[top](#0x00-Shell,-basics)*

---


