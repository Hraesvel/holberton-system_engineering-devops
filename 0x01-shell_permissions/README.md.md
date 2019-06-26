# 0x01. Shell, permissions

**Table Of Context**
- [0. My name is Betty](#0-My-name-is-Betty)
- [1. Who am I](#1-Who-am-I)
- [2. Groups](#2-Groups)
- [3. New owner](#3-New-owner)
- [4. Empty!](#4-Empty!)
- [5. Execute](#5-Execute)
- [6. Multiple permissions](#6-Multiple-permissions)
- [7. Everybody!](#7-Everybody!)
- [8. James Bond](#8-James-Bond)
- [9. John Doe](#9-John-Doe)
- [10. Look in the mirror](#10-Look-in-the-mirror)
- [11. Directories](#11-Directories)
- [12. More directories](#12-More-directories)
- [13. Change group](#13-Change-group)
- [14. Owner and group](#14-Owner-and-group)
- [15. Symbolic links](#15-Symbolic-links)
- [16. If only](#16-If-only)
- [17. Star Wars](#17-Star-Wars)
- [18. RTFM](#18-RTFM)

## Tasks :clipboard:


### 0. My name is Betty
:file_folder: **[0-iam_betty](0-iam_betty)**

This script will change current user ID to `betty`


```
martin@ubuntu:/tmp/h$ tail -1 0-iam_betty | wc -c
9
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---

### 1. Who am I

:file_folder: **[1-who_am_i](1-who_am_i)**

script will print out the current user id


```
martin@ubuntu:/tmp/h$ ./1-who_am_i
martin
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 2. Groups
:file_folder: **[2-groups](2-groups)**

this script will print out all the group that the current user is associated with.


```
martin@ubuntu:/tmp/h$ ./2-groups
martin adm cdrom sudo dip plugdev lpadmin sambashare
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 3. New owner
:file_folder: **[3-new_owner ](3-new_owner )**

script will change the owner of the file `hello` to the user `betty`


```
martin@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 martin martin 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 martin martin  0 Sep 20 14:18 hello
martin@ubuntu:/tmp/h$ sudo ./3-new_owner
martin@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 martin martin 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 betty  martin  0 Sep 20 14:18 hello
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 4. Empty!
:file_folder: **[4-empty](4-empty)**

script that will create an empty file call `hello`.


*[top](#0x01-Shell,-permissions)*

---


### 5. Execute
:file_folder: **[5-execute](5-execute)**

This script will add execution permissions to the owner of the file `hello`.


```
martin@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 martin martin 28 Sep 20 14:26 5-execute
-rw-rw-r-- 1 martin martin 23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$ ./hello
bash: ./hello: Permission denied
martin@ubuntu:/tmp/h$ ./5-execute
martin@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 martin martin 28 Sep 20 14:26 5-execute
-rwxrw-r-- 1 martin martin 23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 6. Multiple permissions
:file_folder: **[6-multiple_permissions](6-multiple_permissions)**

This script will set the permissions of the file `hello` to have execute for owner, and group and read for other users.


```
martin@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 martin martin 36 Sep 20 14:31 6-multiple_permissions
-r--r----- 1 martin martin 23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$ ./6-multiple_permissions
martin@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 martin martin 36 Sep 20 14:31 6-multiple_permissions
-r-xr-xr-- 1 martin martin 23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 7. Everybody!
:file_folder: **[7-everybody](7-everybody)**

This script will set the permissions of the file `hello` to have execute  for all parties.


```
martin@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 martin martin 28 Sep 20 14:35 7-everybody
-rw-r----- 1 martin martin 23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$ ./7-everybody
martin@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 martin martin 28 Sep 20 14:35 7-everybody
-rwxr-x--x 1 martin martin 23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 8. James Bond
:file_folder: **[8-James_Bond](8-James_Bond)**

Script will set permissions to a file `hello` as `007` :sweat_smile:


```
martin@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 martin martin 28 Sep 20 14:40 8-James_Bond
-rwxr-x--x 1 martin martin 23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$ ./8-James_Bond
martin@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 martin martin 28 Sep 20 14:40 8-James_Bond
-------rwx 1 martin martin 23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 9. John Doe
:file_folder: **[9-John_Doe](9-John_Doe)**

A script that set a files permissions to the following below.


<pre><code>-rwxr-x-wx 1 martin martin 23 Sep 20 14:25 hello
</code></pre>

*[top](#0x01-Shell,-permissions)*

---


### 10. Look in the mirror
:file_folder: **[10-mirror_permissions](10-mirror_permissions)**

A script that sets the mode of the file `hello` the same as `olleh`’s mode.

- The file `hello` will be in the working directory
- The file `olleh` will be in the working directory


```
martin@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 martin martin 42 Sep 20 14:45 10-mirror_permissions
-rwxr-x-wx 1 martin martin 23 Sep 20 14:25 hello
-rw-rw-r-- 1 martin martin  0 Sep 20 14:43 olleh
martin@ubuntu:/tmp/h$ ./10-mirror_permissions
martin@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 martin martin 42 Sep 20 14:45 10-mirror_permissions
-rw-rw-r-- 1 martin martin 23 Sep 20 14:25 hello
-rw-rw-r-- 1 martin martin  0 Sep 20 14:43 olleh
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---

### 11. Directories

:file_folder: **[11-directories_permissions](11-directories_permissions)**

script that adds execute permission to all subdirectories of the current directory for  the owner, the group owner and all other users. Regular files should not be changed. 	


```
martin@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 martin martin   24 Sep 20 14:53 11-directories_permissions
drwx------ 2 martin martin 4096 Sep 20 14:49 dir0
drwx------ 2 martin martin 4096 Sep 20 14:49 dir1
drwx------ 2 martin martin 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 martin martin   23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$ ./11-directories_permissions
martin@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 martin martin   24 Sep 20 14:53 11-directories_permissions
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir0
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir1
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 martin martin   23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 12. More directories
:file_folder: **[12-directory_permissions](12-directory_permissions)**

A script that creates a directory called `dir_holberton` with permissions 751 in the working directory.


```
martin@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 martin martin   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir0
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir1
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 martin martin   23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$ ./12-directory_permission s
martin@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 martin martin   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir0
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir1
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir2
drwxr-x--x 2 martin martin 4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 martin martin   23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 13. Change group
:file_folder: **[13-change_group](13-change_group)**

 A script that changes the group owner to `holberton` for the file `hello`

- The file `hello` will be in the working directory


```
martin@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 martin martin   34 Sep 20 15:03 13-change_group
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir0
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir1
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir2
drwxr-x--x 2 martin martin 4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 martin martin   23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$ sudo ./13-change_group
martin@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 martin martin      34 Sep 20 15:03 13-change_group
drwx--x--x 2 martin martin    4096 Sep 20 14:49 dir0
drwx--x--x 2 martin martin    4096 Sep 20 14:49 dir1
drwx--x--x 2 martin martin    4096 Sep 20 14:49 dir2
drwxr-x--x 2 martin martin    4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 martin holberton   23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 14. Owner and group
:file_folder: **[14-change_owner_and_group](14-change_owner_and_group)**

A script that changes the owner to `betty` and the group owner to `holberton` for all the files and directories in the working directory.


```
martin@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 martin martin   36 Sep 20 15:06 14-change_owner_and_group
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir0
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir1
drwx--x--x 2 martin martin 4096 Sep 20 14:49 dir2
drwxr-x--x 2 martin martin 4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 martin martin   23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$ sudo ./14-change_owner_and_group
martin@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 betty holberton   36 Sep 20 15:06 14-change_owner_and_group
drwx--x--x 2 betty holberton 4096 Sep 20 14:49 dir0
drwx--x--x 2 betty holberton 4096 Sep 20 14:49 dir1
drwx--x--x 2 betty holberton 4096 Sep 20 14:49 dir2
drwxr-x--x 2 betty holberton 4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 betty holberton   23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 15. Symbolic links
:file_folder: **[15-symbolic_link_permissions](15-symbolic_link_permissions)**

 A script that changes the owner and the group owner of the file `_hello` to `betty` and `holberton` respectively.

- The file `_hello` is in the working directory
- The file `_hello` is a symbolic link


```
martin@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 martin martin   44 Sep 20 15:12 15-symbolic_link_permissions
-rw-rw-r-- 1 martin martin   23 Sep 20 14:25 hello
lrwxrwxrwx 1 martin martin    5 Sep 20 15:10 _hello -> hello
martin@ubuntu:/tmp/h$ sudo ./15-symbolic_link_permissions
martin@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 martin martin      44 Sep 20 15:12 15-symbolic_link_permissions
-rw-rw-r-- 1 martin martin      23 Sep 20 14:25 hello
lrwxrwxrwx 1 betty  holberton    5 Sep 20 15:10 _hello -> hello
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 16. If only
:file_folder: **[16-if_only ](16-if_only )**

 A script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.

- The file `hello` will be in the working directory


```
martin@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 martin    martin      47 Sep 20 15:18 16-if_only
-rw-rw-r-- 1 guillaume martin      23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$ sudo ./16-if_only
martin@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 martin martin      47 Sep 20 15:18 16-if_only
-rw-rw-r-- 1 betty  martin      23 Sep 20 14:25 hello
martin@ubuntu:/tmp/h$

```



*[top](#0x01-Shell,-permissions)*

---


### 17. Star Wars
:file_folder: **[100-Star_Wars](100-Star_Wars)**

A script that will play the StarWars IV episode in the terminal. But sadly doesn't work anymore because of Disney. :disappointed:


*[top](#0x01-Shell,-permissions)*

---


### 18. RTFM
:file_folder: **[101-man_holberton](101-man_holberton)**

Create a man page.


```
martin@ip-172-31-63-244:/tmp/man$ wc 101-man_holberton
 16  89 608 101-man_holberton
martin@ip-172-31-63-244:/tmp/man$ man ./101-man_holberton

```



*[top](#0x01-Shell,-permissions)*

---


