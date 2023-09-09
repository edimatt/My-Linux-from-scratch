%global debug_package %{nil}
%define _build_id_links none
%define system_name libcap

Name:           EDO%{system_name}
Version:        2.69
Release:        1%{?dist}
Summary:        Library for getting and setting POSIX.1e capabilities.
License:        GPL
Vendor:         %{_vendor}
URL:            https://ftp.osuosl.org/pub/blfs/conglomeration/libcap
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
libcap is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%make_build


%check


%install
%make_install prefix=%_prefix


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_sbindir/*cap*
%_mandir/man*/*cap*
%_mandir/man3/*psx*
%_libdir/%{system_name}.so.2*
%_libdir/%{system_name}.a
%_libdir/libpsx.so.2*
%_libdir/libpsx.a


%files devel
%_includedir/sys/capability.h*
%_includedir/sys/psx_syscall.h
%_libdir/%{system_name}*.so
%_libdir/libpsx.so
%_libdir/pkgconfig/%{system_name}.pc
%_libdir/pkgconfig/libpsx.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
