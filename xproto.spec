%global debug_package %{nil}
%define _build_id_links none
%define system_name xproto

Name:           EDO%{system_name}
Version:        7.0.31
Release:        1%{?dist}
Summary:        X Window System Core Protocol.
License:        GPL
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/proto/xproto
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros
Requires:       glibc
Provides:       %{name} = %{version}
BuildArch:      noarch


%description
This  package  provides  the  headers and specification documents
defining the X Window System Core Protocol, Version 11.
It also includes a number of headers that aren’t purely  protocol
related,  but  are  depended  upon  by many other X Window System
packages to provide common definitions and porting layer.


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


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc specs/x11protocol.xml specs/encoding.xml specs/glossary.xml specs/keysyms.xml specs/sect1-9.xml
%_includedir/X11/*.h
%_libdir/pkgconfig/%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
