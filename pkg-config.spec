%global debug_package %{nil}
%define _build_id_links none
%define _build x86_64-edo-linux-gnu
%define system_name pkg-config

Name:           EDO%{system_name}
Version:        0.29.2
Release:        1%{?dist}
Summary:        A helper tool used when compiling applications and libraries
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.freedesktop.org/wiki/Software/pkg-config
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOpcre-devel EDOkyua
Requires:       glibc EDOpcre
Provides:       %{name} = %{version}


%description
It  helps  you insert the correct compiler options on the command
line so an application can use gcc  ‐o  test  test.c  ‘pkg‐config
‐‐libs  ‐‐cflags  glib‐2.0‘ for instance, rather than hard‐coding
values on where to find glib (or other  libraries).  It  is  lan‐
guage‐agnostic,  so  it  can be used for defining the location of
documentation tools, for instance.

The program is free software and licensed under the GPL version 2
or any later version (at your option).

pkg‐config works on multiple platforms: Linux and other UNIX‐like
operating systems, Mac OS X and Windows. It does not require any‐
thing  but  a reasonably well working C compiler and a C library,
but can use an installed glib if that is present. (A copy of  re‐
cent  glib2  is  shipped  together with pkg‐config versions since
0.27, and this is sufficient for pkg‐config to compile  and  work
properly.)

The  first  implementation  was  written  in shell, by James Hen‐
stridge. Later, it was rewritten in C by Havoc Pennington. It al‐
so  grew  an autoconf macro written by Tim Janik, later rewritten
by Scott James Remnant. The current maintainers  are  Tollef  Fog
Heen tfheen@err.no and Dan Nicholson dbn.lists@gmail.com.


%prep
%setup -n %{system_name}-%{version}
%autoreconf


%build
%set_build_flags_with_rpath
export PKG_CONFIG=/usr/bin/x86_64-redhat-linux-gnu-pkg-config
%_configure --disable-static --build=%_build --with-pc-path=%_libdir/pkgconfig
%make_build


%check
# Requires the kyua framework.
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc %{system_name}-guide.html
%_bindir/%{system_name}
%_bindir/%{_arch}-%{_vendor}*
%_mandir/man1/%{system_name}.1
%_datadir/aclocal/pkg.m4


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
