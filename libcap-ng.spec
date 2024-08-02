%global debug_package %{nil}
%define _build_id_links none
%define system_name libcap-ng

Name:           EDO%{system_name}
Version:        0.8.5
Release:        1%{?dist}
Summary:        Alternate posix capabilities library
License:        LGPL
Vendor:         %{_vendor}
URL:            https://people.redhat.com/sgrubb/libcap-ng
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  EDOgcc glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The libcap‐ng library should make programming with POSIX capabil‐
ities easier. The library has some utilities to help you  analyse
a system for apps that may have too much privileges.
The  included utilities are designed to let admins and developers
spot apps from various ways that may be  running  with  too  much
privilege.


%description devel


%prep
%setup -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%configure
%make_build


%check


%install
%make_install prefix=%_prefix


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*cap*
%_mandir/man*/*cap*
%_mandir/man*/*drop*
%_libdir/%{system_name}.so.0*
%_libdir/libdrop*.so.0*


%files devel
%_includedir/cap-ng.h
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/libdrop*.so
%_libdir/libdrop*.la
%_libdir/pkgconfig/%{system_name}.pc
%_datadir/aclocal/cap-ng.m4


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
