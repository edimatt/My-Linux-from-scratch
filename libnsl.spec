%global debug_package %{nil}
%define _build_id_links none
%define system_name libnsl

Name:           EDO%{system_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Public client interface for NIS(YP).
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/thkukuk/libnsl
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOlibtirpc-devel
Requires:       glibc EDOlibtirpc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
This package contains the libnsl library. This library contains
the public client interface for NIS(YP).
This code was formerly part of glibc, but is now standalone to
be able to link against TI-RPC for IPv6 support.


%description devel


%prep
%setup -n %{system_name}-%{version}
autoupdate
autoreconf -fi


%build
%set_build_flags_with_rpath
%_configure --disable-static --with-libiconv-prefix=%_prefix
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/%{system_name}.so.3*


%files devel
%_includedir/rpcsvc/*
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/%{system_name}.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
