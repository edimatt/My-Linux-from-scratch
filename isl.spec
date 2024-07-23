%global debug_package %{nil}
%define _build_id_links none
%define system_name isl

Name:           EDO%{system_name}
Version:        0.24
Release:        2%{?dist}
Summary:        isl  is  a  thread‐safe C library for manipulating sets and relations of integer points.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.mpfr.org
Source0:        %{system_name}-%{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgmp-devel
Requires:       glibc EDOgmp
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
isl  is  a  thread‐safe C library for manipulating sets and rela‐
tions of integer points bounded by affine constraints.   The  de‐
scriptions  of the sets and relations may involve both parameters
and existentially quantified  variables.   All  computations  are
performed in exact integer arithmetic using GMP.

isl  is  released  under the MIT license, but depends on the LGPL
GMP library.


%description devel


%prep
%setup -n %{system_name}-%{system_name}-%{version}
# We need autoconf v2.69 which is installed in system /usr.
%system_autoreconf


%build
%set_build_flags_with_rpath
%_configure
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/lib%{system_name}.so.23
%_libdir/lib%{system_name}.so.23.1.0


%files devel
%_includedir/%{system_name}/*
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}.la
%_libdir/pkgconfig/%{system_name}.pc
%_libdir/lib%{system_name}.so.23.1.0-gdb.py


%changelog
* Tue Jul 23 2024 Edoardo Di Matteo
- Compile with gcc 14.
* Thu Jan 26 2023 Edoardo Di Matteo
- 
