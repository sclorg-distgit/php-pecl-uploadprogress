This repository contains sources for RPMs that are used
to build Software Collections for CentOS by SCLo SIG.

This branch is for sclo-php7* packages (for rh-php7* SCL)

PHP 7.3 / EL 7

    build -bs *spec --define "scl php73" --define "dist .el7"
    cbs add-pkg   sclo7-sclo-php73-sclo-candidate --owner=sclo  sclo-php73-php-pecl-uploadprogress
    cbs add-pkg   sclo7-sclo-php73-sclo-testing   --owner=sclo  sclo-php73-php-pecl-uploadprogress
    cbs add-pkg   sclo7-sclo-php73-sclo-release   --owner=sclo  sclo-php73-php-pecl-uploadprogress
    cbs build     sclo7-sclo-php73-sclo-el7       <above>.src.rpm
    cbs tag-build sclo7-sclo-php73-sclo-testing   <previous>

PHP 7.2 / EL 7

    build -bs *spec --define "scl php72" --define "dist .el7"
    cbs add-pkg   sclo7-sclo-php72-sclo-candidate --owner=sclo  sclo-php72-php-pecl-uploadprogress
    cbs add-pkg   sclo7-sclo-php72-sclo-testing   --owner=sclo  sclo-php72-php-pecl-uploadprogress
    cbs add-pkg   sclo7-sclo-php72-sclo-release   --owner=sclo  sclo-php72-php-pecl-uploadprogress
    cbs build     sclo7-sclo-php72-sclo-el7       <above>.src.rpm
    cbs tag-build sclo7-sclo-php72-sclo-testing   <previous>

PHP 7.1 / EL 7

    build -bs *spec --define "scl php71" --define "dist .el7"
    cbs add-pkg   sclo7-sclo-php71-sclo-candidate --owner=sclo  sclo-php71-php-pecl-uploadprogress
    cbs add-pkg   sclo7-sclo-php71-sclo-testing   --owner=sclo  sclo-php71-php-pecl-uploadprogress
    cbs add-pkg   sclo7-sclo-php71-sclo-release   --owner=sclo  sclo-php71-php-pecl-uploadprogress
    cbs build     sclo7-sclo-php71-sclo-el7       <above>.src.rpm
    cbs tag-build sclo7-sclo-php71-sclo-testing   <previous>

