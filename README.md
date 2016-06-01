PHP 5.4 / EL 6

    build -bs *spec --define "scl php54" --define "dist .el6"
    cbs add-pkg   sclo6-sclo-php54-sclo-candidate --owner=sclo  sclo-php54-php-pecl-uploadprogress
    cbs add-pkg   sclo6-sclo-php54-sclo-testing --owner=sclo  sclo-php54-php-pecl-uploadprogress
    cbs build     sclo6-sclo-php54-sclo-el6       <above>.src.rpm
    cbs tag-build sclo6-sclo-php54-sclo-testing   <previous>

PHP 5.5 / EL 6

    build -bs *spec --define "scl php55" --define "dist .el6"
    cbs add-pkg sclo6-sclo-php55-sclo-candidate --owner=sclo  sclo-php55-php-pecl-uploadprogress
    cbs build   sclo6-sclo-php55-sclo-el6       <above>.src.rpm

PHP 5.6 / EL 6

    build -bs *spec --define "scl rh-php56" --define "dist .el6"
    cbs add-pkg sclo6-sclo-php56-sclo-candidate --owner=sclo  sclo-php56-php-pecl-uploadprogress
    cbs build   sclo6-sclo-php56-sclo-el6       <above>.src.rpm

PHP 5.4 / EL 7

    build -bs *spec --define "scl php54" --define "dist .el7"
    cbs add-pkg sclo7-sclo-php54-sclo-candidate --owner=sclo  sclo-php54-php-pecl-uploadprogress
    cbs build   sclo7-sclo-php54-sclo-el7       <above>.src.rpm

PHP 5.5 / EL 7

    build -bs *spec --define "scl php55" --define "dist .el7"
    cbs add-pkg sclo7-sclo-php55-sclo-candidate --owner=sclo  sclo-php55-php-pecl-uploadprogress
    cbs build   sclo7-sclo-php55-sclo-el7       <above>.src.rpm

PHP 5.6 / EL 7

    build -bs *spec --define "scl rh-php56" --define "dist .el7"
    cbs add-pkg sclo7-sclo-php56-sclo-candidate --owner=sclo  sclo-php56-php-pecl-uploadprogress
    cbs build   sclo7-sclo-php56-sclo-el7       <above>.src.rpm
