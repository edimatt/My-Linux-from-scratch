%global debug_package %{nil}
%define _build_id_links none
%define system_name mpfr

Name:           EDO%{system_name}
Version:        4.2.0
Release:        1%{?dist}
Summary:        C library for multiple-precision floating-point computations.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.mpfr.org
Source0:        %{system_name}-%{version}.tar.xz
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
The  %{system_name} library is a C library for multiple‐precision
floating‐point computations with "correct rounding". The MPFR  is
efficient  and  also  has a well‐defined semantics. It copies the
good ideas from the ANSI/IEEE‐754 standard  for  double‐precision
floating‐point arithmetic (53‐bit mantissa). MPFR is based on the
GMP multiple‐precision library.


%description devel
The  libraries,  header files and documentation for using the GNU
%{system_name} library in applications.

If you want to develop applications which will use the GNU 
%{system_name}. You will need to install the %{system_name} devel
package. You will also need to install the %{system_name} package.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/lib%{system_name}.a
%_libdir/lib%{system_name}.la
%_libdir/lib%{system_name}.so.6
%_libdir/lib%{system_name}.so.6.2.0


%files devel
%_docdir/%{system_name}/*
%_includedir/%{system_name}.h
%_includedir/mpf2%{system_name}.h
%_libdir/lib%{system_name}.so
%_libdir/pkgconfig/%{system_name}.pc
%_infodir/%{system_name}.info*
%ghost %{_infodir}/dir


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
