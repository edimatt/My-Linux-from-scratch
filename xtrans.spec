%global debug_package %{nil}
%define _build_id_links none
%define system_name xtrans

Name:           EDO%{system_name}
Version:        1.5.0
Release:        1%{?dist}
Summary:        X Network Transport layer shared code
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/lib/libxtrans
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros
Requires:       glibc
Provides:       %{name} = %{version}
BuildArch:      noarch


%description
xtrans  is a library of code that is shared among various X pack‐
ages to handle network protocol transport in a  modular  fashion,
allowing  a  single place to add new transport types.  It is used
by the X server, libX11, libICE, the X font server,  and  related
components.   It is however, NOT a shared library, but code which
each consumer includes and builds it’s own copy of  with  various
ifdef  flags  to  make  each copy slightly different.  To support
this in the modular build system, this  package  simply  installs
the C source files into $(prefix)/include/X11/Xtrans and installs
a pkg‐config file and an autoconf m4 macro file  with  the  flags
needed  to  use it.  Documentation of the xtrans API can be found
in the included xtrans.xml file in DocBook XML format. If ’xmlto’
is installed, you can generate text, html, postscript or pdf ver‐
sions of the documentation by configuring the  build  with  ‐‐en‐
able‐docs, which is the default.


%prep
%setup -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%check


%install
%make_install
%__mkdir_p %{buildroot}%{_libdir}/pkgconfig
%__mv %{buildroot}%{_datadir}/pkgconfig/* %{buildroot}%{_libdir}/pkgconfig/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc doc/xtrans.xml
%_includedir/X11/Xtrans/*
%_datadir/aclocal/%{system_name}.m4
%_libdir/pkgconfig/%{system_name}.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
/home/edoardo/rpmbuild/BUILDROOT/EDOxtrans-1.5.0-1.el9.x86_64/opt/edo/share/pkgconfig
/home/edoardo/rpmbuild/BUILDROOT/EDOxtrans-1.5.0-1.el9.x86_64/opt/edo/share/pkgconfig/xtrans.pc
