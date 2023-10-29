%global debug_package %{nil}
%define _build_id_links none
%define system_name kbproto

Name:           EDO%{system_name}
Version:        1.0.7
Release:        1%{?dist}
Summary:        X Keyboard Extension.
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/proto/kbproto
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros
Requires:       glibc
Provides:       %{name} = %{version}
BuildArch:      noarch


%description
This extension defines a protcol to provide a number of new capabilities
and controls for text keyboards.

Extension name: XKEYBOARD

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
# Provided by libX11.
%__rm %{buildroot}%{_includedir}/X11/extensions/XKBgeom.h


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_docdir/%{name}/*
%_includedir/X11/extensions/*.h
%_libdir/pkgconfig/%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
