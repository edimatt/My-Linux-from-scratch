%global debug_package %{nil}
%define _build_id_links none


Name:           sqlite
Version:        3.40.1
Release:        1%{?dist}
Summary:        Library that implements an embeddable SQL database engine.
License:        GPL
URL:            https://github.com/vim/vim
Source0:        %{name}-version-%{version}.tar.gz
BuildRequires:  glibc-devel ncurses-devel zlib-devel readline-devel
Requires:       sqlite-libs readline
AutoReqProv:    no


%package libs
Summary:        Shared library for the sqlite3 embeddable SQL database engine.
Requires:       zlib ncurses-libs glibc
AutoReqProv:    no


%package devel
Summary:        Development tools for the sqlite3 embeddable SQL database engine.
Requires:       sqlite-libs
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
%setup -n %{name}-version-%{version}


%build
%set_build_flags_with_rpath
%configure --enable-static=no
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{name}3


%files libs
%_libdir/lib%{name}3.so.0
%_libdir/lib%{name}3.so.0.8.6


%files devel
%_includedir/%{name}3.h
%_includedir/%{name}3ext.h
%_libdir/lib%{name}3.so
%_libdir/pkgconfig/%{name}3.pc
%_libdir/lib%{name}3.la


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
