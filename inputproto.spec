%global debug_package %{nil}
%define _build_id_links none
%define system_name inputproto

Name:           EDO%{system_name}
Version:        2.3.2
Release:        1%{?dist}
Summary:        X Input Extension.
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/proto/inputproto
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros
Requires:       glibc
Provides:       %{name} = %{version}
BuildArch:      noarch


%description
This extension defines a protocol to provide additional input devices
management such as graphic tablets.

Extension name: XInputExtension


%prep
%setup -q -n %{system_name}-%{version}
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
%_docdir/%{name}/*
%_includedir/X11/extensions/*.h
%_libdir/pkgconfig/%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
