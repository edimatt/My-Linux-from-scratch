%global debug_package %{nil}
%define _build_id_links none
%define system_name gdbm

Name:           EDO%{system_name}
Version:        1.23
Release:        1%{?dist}
Summary:        A GNU set of database routines which use extensible hashing.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.gnu.org.ua/software/gdbm/
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOreadline-devel EDOncurses-devel
Requires:       glibc EDOreadline EDOncurses-libs %{name}-libs
Provides:       %{name} = %{version}


%package libs
Summary:        Libraries files for the %{system_name} library.
Requires:       glibc
Provides:       %{name}-libs = %{version}
AutoReqProv:    no


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name}-libs = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
GNU  dbm  (or GDBM, for short) is a library of database functions
that use extensible hashing and work similar to the standard UNIX
dbm.  These routines are provided to a programmer needing to cre‐
ate and manipulate a hashed database.

The basic use of GDBM is to store key/data pairs in a data  file.
Each key must be unique and each key is paired with only one data
item.

The library  provides  primitives  for  storing  key/data  pairs,
searching  and  retrieving the data by its key and deleting a key
along with its data. It also support  sequential  iteration  over
all key/data pairs in a database.

For  compatibility with programs using old UNIX dbm function, the
package also provides traditional dbm and ndbm interfaces.

GNU gdbm is written by Philip A. Nelson, Jason Downs  and  Sergey
Poznyakoff.


%description libs
Libraries for the Gdbm GNU database indexing library


%description devel
Gdbm‐devel  contains  the  development libraries and header files
for gdbm, the GNU database system.  These  libraries  and  header
files  are necessary if you plan to do development using the gdbm
database.

Install gdbm‐devel if you are developing C  programs  which  will
use  the  gdbm database library.  You’ll also need to install the
gdbm package.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --disable-static --enable-libgdbm-compat
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}*
%_mandir/man1/%{system_name}*.1
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%files libs
%_libdir/lib%{system_name}.so.6*
%_libdir/lib%{system_name}_compat.so.4*


%files devel
%_includedir/%{system_name}.h
%_includedir/*dbm.h
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}.la
%_libdir/lib%{system_name}_compat.so
%_libdir/lib%{system_name}_compat.la
%_mandir/man3/%{system_name}.3
%ghost %_infodir/dir
%_infodir/%{system_name}.info


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
