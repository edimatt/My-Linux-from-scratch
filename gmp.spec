%global debug_package %{nil}
%define _build_id_links none
%define system_name gmp

Name:           EDO%{system_name}
Version:        6.3.0
Release:        1%{?dist}
Summary:        A GNU arbitrary precision library.
License:        GPL
Vendor:         %{_vendor}
URL:            https://gmplib.org
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
AutoReqProv:    no


%description
The  gmp  package contains GNU MP, a library for arbitrary preci‐
sion arithmetic, signed integers operations, rational numbers and
floating  point  numbers.  GNU MP is designed for speed, for both
small and very large operands. GNU MP is  fast  because  it  uses
fullwords  as the basic arithmetic type, it uses fast algorithms,
it carefully optimizes assembly code for many CPUs’  most  common
inner  loops,  and  it  generally emphasizes speed over simplici‐
ty/elegance in its operations.

Install the gmp package if you need a  fast  arbitrary  precision
library.


%description devel
The  libraries,  header files and documentation for using the GNU
MP arbitrary precision library in applications.

If you want to develop applications which will use the GNU MP li‐
brary, you’ll need to install the gmp‐devel package.  You’ll also
need to install the gmp package.


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
%_libdir/lib%{system_name}.so.10
%_libdir/lib%{system_name}.so.10.5.0


%files devel
%_includedir/%{system_name}.h
%_libdir/lib%{system_name}.so
%_libdir/pkgconfig/%{system_name}.pc
%_infodir/%{system_name}.info*
%ghost %{_infodir}/dir


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
