%global debug_package %{nil}
%define _build_id_links none
%define system_name acl

Name:           EDO%{system_name}
Version:        2.3.1
Release:        1%{?dist}
Summary:        Dynamic library for access control list support.
License:        GPL
Vendor:         %{_vendor}
URL:            https://download-mirror.savannah.gnu.org/releases/acl
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOattr-devel
Requires:       glibc EDOattr %{name}-libs
Provides:       %{name} = %{version}


%package libs
Summary:        Development tools for the %{system_name} library.
Requires:       glibc EDOattr-libs
Provides:       %{name}-libs = %{version}
AutoReqProv:    no


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name}-libs = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
This package contains the getfacl and setfacl utilities needed for
manipulating access control lists.


%description libs
This  package  contains  the libacl.so dynamic library which con‐
tains the POSIX 1003.1e draft standard 17 functions  for  manipu‐
lating access control lists.


%description devel
This package contains header files and documentation needed to develop
programs which make use of the access control list programming interface
defined in POSIX 1003.1e draft standard 17.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc CHANGES COPYING COPYING.LGPL
%_bindir/chacl
%_bindir/getfacl
%_bindir/setfacl
%_mandir/man1/chacl.1
%_mandir/man1/getfacl.1
%_mandir/man1/setfacl.1
%_mandir/man5/acl.5
%_datadir/locale/en@boldquot/LC_MESSAGES/acl.mo
%_datadir/locale/en@quot/LC_MESSAGES/acl.mo
%_datadir/locale/de/LC_MESSAGES/acl.mo
%_datadir/locale/es/LC_MESSAGES/acl.mo
%_datadir/locale/fr/LC_MESSAGES/acl.mo
%_datadir/locale/gl/LC_MESSAGES/acl.mo
%_datadir/locale/pl/LC_MESSAGES/acl.mo
%_datadir/locale/sv/LC_MESSAGES/acl.mo


%files libs
%_docdir/%{name}/libacl.txt
%_docdir/%{name}/PORTING
%_docdir/%{name}/extensions.txt
%_libdir/lib%{system_name}.so.1
%_libdir/lib%{system_name}.so.1.1.2301


%files devel
%_includedir/%{system_name}/lib%{system_name}.h
%_includedir/sys/%{system_name}.h
%_libdir/pkgconfig/lib%{system_name}.pc
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}.la
%_mandir/man3/%{system_name}_*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
