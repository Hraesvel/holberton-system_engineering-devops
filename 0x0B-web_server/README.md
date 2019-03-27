# 0x0B. Web server


**TOC**
- [0. Transfer a file to your server](#0-Transfer-a-file-to-your-server)
- [1. Install nginx web server](#1-Install-nginx-web-server)
- [2. Setup a domain name](#2-Setup-a-domain-name)
- [3. Redirection](#3-Redirection)
- [4. Not found page 404](#4-Not-found-page-404)
- [5. Design a beautiful 404 page](#5-Design-a-beautiful-404-page)
- [6. Deploy fast, deploy well](#6-Deploy-fast,-deploy-well)


## Tasks


### 0. Transfer a file to your server
File: **[0-transfer_file](0-transfer_file)**




```
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$

```



---


### 1. Install nginx web server
File: **[1-install_nginx_web_server](1-install_nginx_web_server)**

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/nginx-master-yoda.jpg)

Readme:

* [-y on apt-get command](/rltoken/qU2tVilKLygFZcRpEWD3lw)

Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

* Install `nginx` on your `web-01` server
* Nginx should be listening on port 80
* When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Holberton School`
* As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

Example:

In this example `34.198.248.145` is the IP of my `web-01` server. If you want to query the Nginx that is locally installed on your server, you can use `curl 127.0.0.1`.

If things are not going as expected, make sure to check out Nginx logs, they can be found in `/var/log/`.

**Repo:**

* GitHub repository: `holberton-system_engineering-devops`
* Directory: `0x0B-web_server`
* File: `1-install_nginx_web_server`

Each container will be available 24h max


```
sylvain@ubuntu$ curl 34.198.248.145/
Holberton School for the win!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: &quot;58abea7c-1e&quot;
Accept-Ranges: bytes

sylvain@ubuntu$

```



---


### 2. Setup a domain name
File: **[2-setup_a_domain_name](2-setup_a_domain_name)**




```
sylvain@ubuntu$ cat 2-setup_a_domain_name
holberton.online
sylvain@ubuntu$
sylvain@ubuntu$ dig holberton.online

; &lt;&lt;&gt;&gt; DiG 9.9.5-3ubuntu0.8-Ubuntu &lt;&lt;&gt;&gt; holberton.online
;; global options: +cmd
;; Got answer:
;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 10447
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;holberton.online.          IN  A

;; ANSWER SECTION:
holberton.online.       298 IN  A   34.198.248.145

;; Query time: 313 msec
;; SERVER: 10.0.2.3#53(10.0.2.3)
;; WHEN: Tue Feb 21 22:21:22 UTC 2017
;; MSG SIZE  rcvd: 57

sylvain@ubuntu$

```



---


### 3. Redirection
File: **[3-redirection](3-redirection)**

Readme:

* [Replace a line with multiple lines with sed](/rltoken/Afg1zCifjmIygL1se0ghhg)

Configure your Nginx server so that `/redirect_me` is redirecting to another page.

Requirements:

* The redirection must be a “301 Moved Permanently”
* You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
* Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task

Example:

**Repo:**

* GitHub repository: `holberton-system_engineering-devops`
* Directory: `0x0B-web_server`
* File: `3-redirection`

Each container will be available 24h max


```
sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$

```



---


### 4. Not found page 404
File: **[4-not_found_page_404](4-not_found_page_404)**

Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.

Requirements:

* The page must return an HTTP 404 error code
* The page must contain the string `Ceci n'est pas une page`
* Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task

Example:

**Repo:**

* GitHub repository: `holberton-system_engineering-devops`
* Directory: `0x0B-web_server`
* File: `4-not_found_page_404`

Each container will be available 24h max


```
sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: &quot;58acb50e-1a&quot;

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page

sylvain@ubuntu$

```



---


### 5. Design a beautiful 404 page
File: **[5-design_a_beautiful_404_page](5-design_a_beautiful_404_page)**




---


### 6. Deploy fast, deploy well
File: **[fabfile.py](fabfile.py)**




```
sylvain@ubuntu$ ls
0-transfer_file  1-install_nginx_web_server  2-setup_a_domain_name  3-redirection  4-404  fabfile.py  holberton  README.md
sylvain@ubuntu$ fab pack
[localhost] local: tar --exclude='*.tar.gz' -cvzf holbertonwebapp.tar.gz .
./
./README.md
./0-transfer_file
./1-install_nginx_web_server
./2-setup_a_domain_name
./3-redirection
./4-404
./fabfile.py
./fabfile.pyc
./holberton
./README.md

Done.
sylvain@ubuntu$ ls
0-transfer_file  1-install_nginx_web_server  2-setup_a_domain_name  3-redirection  4-404  fabfile.py  fabfile.pyc  holberton  holbertonwebapp.tar.gz  README.md
sylvain@ubuntu$ fab deploy -H 34.198.248.145 | grep -v 34.198.248.145
/usr/lib/python2.7/dist-packages/Crypto/Cipher/blockalgo.py:141: FutureWarning: CTR mode needs counter parameter, not IV
  self._cipher = factory.new(key, *args, **kwargs)

Done.
sylvain@ubuntu$ ssh ubuntu@34.198.248.145 'ls /tmp/'
holbertonwebapp
holbertonwebapp.tar.gz
sylvain@ubuntu$ ssh ubuntu@34.198.248.145 'ls /tmp/holbertonwebapp/'
0-transfer_file
1-install_nginx_web_server
2-setup_a_domain_name
3-redirection
4-404
fabfile.py
fabfile.pyc
holberton
README.md
sylvain@ubuntu$ fab clean
[localhost] local: rm holbertonwebapp.tar.gz

Done.
sylvain@ubuntu$ ls
0-transfer_file  1-install_nginx_web_server  2-setup_a_domain_name  3-redirection  4-404  fabfile.py  fabfile.pyc  holberton  README.md
sylvain@ubuntu$

```



---


