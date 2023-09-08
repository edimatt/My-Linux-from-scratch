%global debug_package %{nil}
%define _build_id_links none
%define system_name sqlite

Name:           EDO%{system_name}
Version:        3.40.1
Release:        1%{?dist}
Summary:        Library that implements an embeddable SQL database engine.
License:        GPL
URL:            https://www.sqlite.org/index.html
Source0:        %{system_name}-version-%{version}.tar.gz
Provides:       %{name}-%{version}
BuildRequires:  glibc-devel EDOncurses-devel EDOzlib-devel EDOreadline-devel
Requires:       sqlite-libs EDOreadline %{name}-libs = %{version}
AutoReqProv:    no


%package libs
Summary:        Shared library for the sqlite3 embeddable SQL database engine.
Provides:       %{name}-libs = %{version}
Requires:       EDOzlib EDOncurses-libs glibc
AutoReqProv:    no


%package devel
Summary:        Development tools for the sqlite3 embeddable SQL database engine.
Provides:       %{name}-devel = %{version}
Requires:       %{name}-libs = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
SQLite   is  a  C library that implements an SQL database engine.
A large subset of SQL92  is  supported.  A  complete  database is
stored in a single disk file. The API is designed for convenience
and ease of  use.   Applications  that  link  against SQLite  can
enjoy  the  power and flexibility of an SQL database  without the
administrative hassles of supporting a  separate database server.
Version 2 and version 3 binaries are named to  permit each  to be 
installed on a single host.


%description libs
This package contains the shared library for sqlite.


%description devel
This package contains the header files and development documenta‐
tion for sqlite. If you like to develop  programs  using  sqlite,
you will need to install sqlite‐devel.


%prep
%setup -n %{system_name}-version-%{version}


%build
%set_build_flags_with_rpath
%configure --enable-static=no --with-tcl=/usr/lib64 TCLLIBDIR=%_datadir/tcl8.6/sqlite3
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}3


%files libs
%_libdir/lib%{system_name}3.so.0
%_libdir/lib%{system_name}3.so.0.8.6
%_datadir/tcl8.6/sqlite3/libtclsqlite3.so


%files devel
%_includedir/%{system_name}3.h
%_includedir/%{system_name}3ext.h
%_libdir/lib%{system_name}3.so
%_libdir/pkgconfig/%{system_name}3.pc
%_libdir/lib%{system_name}3.la
%_datadir/tcl8.6/sqlite3/pkgIndex.tcl

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
