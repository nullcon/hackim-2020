FROM php:7.1.8-apache


COPY public/ /var/www/html/

RUN chown -R www-data:www-data /var/www/html \
    && a2enmod rewrite

