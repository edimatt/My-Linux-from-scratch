%global debug_package %{nil}
%define _build_id_links none
%define system_name xextproto

Name:           EDO%{system_name}
Version:        7.3.0
Release:        1%{?dist}
Summary:        X Protocol Extensions.
License:        GPL
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/proto/xextproto
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros
Requires:       glibc
Provides:       %{name} = %{version}
BuildArch:      noarch


%description
Extension names:

DOUBLE-BUFFER
DPMS
Extended-Visual-Information
Generic Event Extension
LBX
MIT-SHM
MIT-SUNDRY-NONSTANDARD
Multi-Buffering
SECURITY
SHAPE
SYNC
TOG-CUP
XC-APPGROUP
XTEST


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
%_docdir/%{name}/*.xml
%_includedir/X11/extensions/*.h
%_libdir/pkgconfig/%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
