coop-coffees-members
====================

Ubuntu
------

::

    sudo apt-get update
    sudo apt-get install aptitude build-essential libjpeg-dev libxslt-dev \
        libreadline-dev                                                   \
        libsslcommon2-dev libssl-dev libtiff5-dev libjpeg8-dev            \
        libfreetype6-dev liblcms2-dev libwebp-dev libssl-dev libxml2-dev  \
        libxslt1-dev libbz2-dev nginx openssl python-dev tcl8.6-dev       \
        tk8.6-dev zlib1g-dev -y
    sudo aptitude update
    sudo aptitude upgrade -y

Plone + Python
--------------

::

    git clone git@github.com:ACLARKNET/coop-coffees-members.git
    sudo mv coop-coffees-members /srv/
    cd /srv/coop-coffees-members
    tar zxvf Python-2.4.6.tgz
    cd Python-2.4.6

For SSL support, add ``/usr/lib/x86_64-linux-gnu`` to line 271 of ``setup.py``.

::

    ./configure
    make
    sudo make install


NGINX
-----

/etc/nginx/sites-enabled/default
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
            proxy_pass http://localhost:8080/VirtualHostBase/http/members.coopcoffees.com:80/coopcoffees/VirtualHostRoot/;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }
    }
