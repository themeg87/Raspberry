# wordpress (포테이너설치)
<pre><code>
  version: '2.1'
services:
  wordpress:
    image: wordpress
    restart: always
    ports:
      - 9999:80
    environment:
      PUID: 1000
      PGID: 100
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: changeme
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - /PATH TO FOLDER/wordpress:/var/www/html
    links:
      - db:db
  db:
    image: ghcr.io/linuxserver/mariadb
    environment:
      - PUID=1000
      - PGID=100
      - MYSQL_ROOT_PASSWORD=changeme
      - TZ=Europe/London
      - MYSQL_DATABASE=wordpress
      - MYSQL_USER=wordpress
      - MYSQL_PASSWORD=changeme #Must match the above password
    volumes:
      - /PATH TO FOLDER/Wordpressdb:/config
    ports:
      - 3333:3306
    restart: unless-stopped
volumes:
  wordpress:
  db:
</code></pre>
