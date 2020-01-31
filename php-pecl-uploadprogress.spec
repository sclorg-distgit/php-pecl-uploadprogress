# centos/sclo spec file for php-pecl-uploadprogress, from:
#
# remirepo spec file for php-pecl-uploadprogress
#
# Copyright (c) 2013-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%if 0%{?scl:1}
%global sub_prefix sclo-%{scl_prefix}
%if "%{scl}" == "rh-php73"
%global sub_prefix sclo-php73-
%endif
%if "%{scl}" == "rh-php72"
%global sub_prefix sclo-php72-
%endif
%scl_package      php-pecl-uploadprogress
%endif

%global pecl_name uploadprogress
%global ini_name  40-%{pecl_name}.ini

Summary:        An extension to track progress of a file upload
Name:           %{?sub_prefix}php-pecl-%{pecl_name}
Version:        1.1.3
Release:        2%{?dist}
License:        PHP
Group:          Development/Languages
URL:            http://pecl.php.net/package/%{pecl_name}
Source0:        http://pecl.php.net/get/%{pecl_name}-%{version}.tgz

BuildRequires:  %{?scl_prefix}php-devel
BuildRequires:  %{?scl_prefix}php-pear

Requires:       %{?scl_prefix}php(zend-abi) = %{php_zend_api}
Requires:       %{?scl_prefix}php(api) = %{php_core_api}

Provides:       %{?scl_prefix}php-%{pecl_name}               = %{version}
Provides:       %{?scl_prefix}php-%{pecl_name}%{?_isa}       = %{version}
Provides:       %{?scl_prefix}php-pecl(%{pecl_name})         = %{version}
Provides:       %{?scl_prefix}php-pecl(%{pecl_name})%{?_isa} = %{version}
Provides:       %{?scl_prefix}php-pecl-%{pecl_name}          = %{version}-%{release}
Provides:       %{?scl_prefix}php-pecl-%{pecl_name}%{?_isa}  = %{version}-%{release}

%if 0%{?fedora} < 20 && 0%{?rhel} < 7
# Filter shared private
%{?filter_provides_in: %filter_provides_in %{_libdir}/.*\.so$}
%{?filter_setup}
%endif


%description
A PHP extension to track progress of a file upload, including details
on the speed of the upload, estimated time remaining, and access to
the contents of the file as it is being uploaded

It requires the use of the Apache HTTP Server with mod_php.
Other web servers and PHP-FPM are not yet supported.

Package built for PHP %(%{__php} -r 'echo PHP_MAJOR_VERSION.".".PHP_MINOR_VERSION;')%{?scl: as Software Collection (%{scl} by %{?scl_vendor}%{!?scl_vendor:rh})}.


%prep
%setup -q -c
mv %{pecl_name}-%{version} NTS

%{?_licensedir:sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml}

cd NTS
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_UPLOADPROGRESS_VERSION/{s/.* "//;s/".*$//;p}' php_uploadprogress.h)
if test "x${extver}" != "x%{version}%{?prever:-%{prever}}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever:-%{prever}}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so

; Runtime configuration options
;uploadprogress.file.filename_template = '/tmp/upt_%%s.txt'
;uploadprogress.file.contents_template = '/tmp/upload_contents_%%s'
;uploadprogress.get_contents = 0
EOF


%build
cd NTS
%{_bindir}/phpize
%configure \
    --with-libdir=%{_lib} \
    --with-php-config=%{_bindir}/php-config

make %{?_smp_mflags}


%install
make -C NTS install INSTALL_ROOT=%{buildroot}

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Documentation
for i in %{!?_licensedir:LICENSE} $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


# when pear installed alone, after us
%triggerin -- %{?scl_prefix}php-pear
if [ -x %{__pecl} ] ; then
    %{pecl_install} %{pecl_xmldir}/%{name}.xml >/dev/null || :
fi

# posttrans as pear can be installed after us
%posttrans
if [ -x %{__pecl} ] ; then
    %{pecl_install} %{pecl_xmldir}/%{name}.xml >/dev/null || :
fi

%postun
if [ $1 -eq 0 -a -x %{__pecl} ] ; then
    %{pecl_uninstall} %{pecl_name} >/dev/null || :
fi


%check
: Minimal load test for NTS extension
cd NTS
%{__php} --no-php-ini \
    --define extension=modules/%{pecl_name}.so \
    --modules | grep %{pecl_name}


%files
%{?_licensedir:%license NTS/LICENSE}
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Fri Jan 31 2020 Remi Collet <remi@remirepo.net> - 1.1.3-2
- update to 1.1.3
- improve description

* Mon Jan 27 2020 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2

* Mon Oct 28 2019 Remi Collet <remi@remirepo.net> - 1.0.3.1-5
- build for sclo-php73

* Thu Nov 15 2018 Remi Collet <remi@remirepo.net> - 1.0.3.1-4
- build for sclo-php72

* Thu Aug 10 2017 Remi Collet <remi@remirepo.net> - 1.0.3.1-3
- change for sclo-php71

* Thu Nov  3 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3.1-2
- add patch for PHP 7

* Wed Jun  1 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3.1-1
- cleanup for SCLo build

* Tue Jun 23 2015 Remi Collet <remi@fedoraproject.org> - 1.0.3.1-7
- allow build against rh-php56 (as more-php56)
- rebuild for "rh_layout" (php70)

* Thu Apr  9 2015 Remi Collet <remi@fedoraproject.org> - 1.0.3.1-6
- add fix for PHP 7
- drop runtime dependency on pear, new scriptlets

* Wed Dec 24 2014 Remi Collet <remi@fedoraproject.org> - 1.0.3.1-5.1
- Fedora 21 SCL mass rebuild

* Tue Aug 26 2014 Remi Collet <rcollet@redhat.com> - 1.0.3.1-5
- improve SCL build

* Thu Apr 17 2014 Remi Collet <remi@fedoraproject.org> - 1.0.3.1-4
- add numerical prefix to extension configuration file (php 5.6)

* Tue Mar 25 2014 Remi Collet <remi@fedoraproject.org> - 1.0.3.1-3
- allow SCL build

* Tue Nov  5 2013 Remi Collet <remi@fedoraproject.org> - 1.0.3.1-2
- cleanups for Copr
- install doc in pecl doc_dir

* Sat Oct 12 2013 Remi Collet <remi@fedoraproject.org> - 1.0.3.1-1
- initial package, version 1.0.3.1 (stable)

