%global debug_package %{nil}
%define _build_id_links none
%define system_name lutok

Name:           EDO%{system_name}
Version:        0.4
Release:        1%{?dist}
Summary:        Lightweight C++ API library for Lua.
License:        GPL
URL:            https://github.com/jmmv/lutok
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build EDOgcc EDOlua-devel EDOlibiconv-devel
Requires:       glibc EDOlua-libs EDOlibiconv
AutoReqProv:    no


%description
Lutok provides thin C++ wrappers around the Lua C API to ease the
interaction between C++ and Lua.  These wrappers  make  intensive
use of RAII to prevent resource leakage, expose C++‐friendly data
types, report errors by means of exceptions and ensure  that  the
Lua  stack  is  always left untouched in the face of errors.  The
library also provides a small  subset  of  miscellaneous  utility
functions built on top of the wrappers.

Lutok  focuses  on  providing a clean and safe C++ interface; the
drawback is that it is not suitable for performance‐critical  en‐
vironments.  In order to implement error‐safe C++ wrappers on top
of a Lua C binary library, Lutok adds several layers or  abstrac‐
tion  and  error  checking that go against the original spirit of
the Lua C API and thus degrade performance.

For further information on  the  contents  of  this  distribution
file, please refer to the following other documents:

*  AUTHORS: List of authors and contributors to this project.
*  COPYING: License information.
*  INSTALL: Compilation and installation instructions.
*     NEWS: List of major changes between formal releases.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure
%make_build


%install
%make_install
mv %{buildroot}%{_prefix}/tests/%{system_name} %{buildroot}%{_datadir}/%{system_name}

%check
# make check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/lib%{system_name}*
%_libdir/pkgconfig/%{system_name}.pc
%_docdir/%{system_name}/*
%_includedir/%{system_name}/*
%_datadir/%{system_name}/*

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
