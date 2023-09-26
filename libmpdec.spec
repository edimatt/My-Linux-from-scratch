%global debug_package %{nil}
%define __brp_strip_lto %{nil}
%define _build_id_links none
%define system_name mpdecimal

Name:           EDO%{system_name}
Version:        2.5.1
Release:        1%{?dist}
Summary:        Library for correctly-rounded arbitrary precision decimal floating point arithmetic.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.bytereef.org/mpdecimal
Source0:        %{system_name}-%{version}.tar.gz
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
libmpdec  is  a  complete  implementation  of the General Decimal
Arithmetic Specification.  The  specification,  written  by  Mike
Cowlishaw from IBM, defines a general purpose arbitrary precision
data type together with rigorously specified functions and round‐
ing behavior. As described in the scope section of the specifica‐
tion, libmpdec will ‐ with minor restrictions ‐ also  conform  to
the IEEE 754‐2008 Standard for Floating‐Point Arithmetic, provid‐
ed that the appropriate context parameters are set.
libmpdec is written in C, but the header files are  prepared  for
use with a C++ compiler.
Starting from Python‐3.3, libmpdec is the basis for Python's dec‐
imal module.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --enable-shared --enable-profile
%make_build


%check
# make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/libmpdec*.so.*
%_libdir/libmpdec*.a


%files devel
%_includedir/*decimal*.h*
%_libdir/libmpdec*.so
%_docdir/%{system_name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
