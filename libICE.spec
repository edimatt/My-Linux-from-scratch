%global debug_package %{nil}
%define _build_id_links none
%define system_name libICE

Name:           EDO%{system_name}
Version:        1.1.1
Release:        1%{?dist}
Summary:        The Inter-Client Exchange library
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/lib/libice
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxproto EDOxtrans
Requires:       glibc

Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
There  are  numerous  possible  inter‐client protocols, with many
similarities and common needs ‐ authentication, version  negotia‐
tion,  byte  order  negotiation,  and so on. The Inter‐Client Ex‐
change (ICE) protocol is intended  to  provide  a  framework  for
building  such protocols, allowing them to make use of common ne‐
gotiation mechanisms and to be multiplexed over a  single  trans‐
port connection.


%description devel


%prep
%setup -n %{system_name}-%{version}
./autogen.sh


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
%_libdir/%{system_name}.so.6*


%files devel
%_includedir/X11/ICE/*
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/ice.pc
%_docdir/%{name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
