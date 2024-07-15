%global debug_package %{nil}
%define _build_id_links none
%define system_name date

Name:           EDO%{system_name}
Version:        3.0.1
Release:        1%{?dist}
Summary:        A date library for C++ based on chrono.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/HowardHinnant/date
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc EDOlibevent-devel EDOlibiconv-devel 
Requires:       glibc EDOgcc EDOpcre cyrus-sasl-lib EDObrotli-libs EDOkrb5 EDOlibevent EDOlibiconv EDOlibidn2 EDOlibpsl EDOlibunistring EDOlibxcrypt EDOnghttp2 EDOopenssl-libs EDOzlib libcom_err libcurl libssh openldap
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
This is actually several separate C++11/C++14/C++17 libraries:

"date.h"  is a header‐only library which builds upon <chrono>. It
adds some new duration types, and new time_point types.  It  also
adds  "field"  types  such  as  year_month_day  which is a struct
{year, month, day}. And it provides convenient means  to  convert
between the "field" types and the time_point types.
Documentation:      http://howardhinnant.github.io/date/date.html
Video:    https://www.youtube.com/watch?v=tzyGjOm8AKo     Slides:
http://schd.ws/hosted_files/cppcon2015/43/hinnant_dates.pdf

"tz.h" / "tz.cpp" are a timezone library  built  on  top  of  the
"date.h"  library.  This timezone library is a complete parser of
the IANA timezone database. It provides for an easy way to access
all  of  the data in this database, using the types from "date.h"
and <chrono>. The IANA database also includes data on  leap  sec‐
onds,  and  this  library provides utilities to compute with that
information as well.
Documentation: http://howardhinnant.github.io/date/tz.html
Video: https://www.youtube.com/watch?v=Vwd3pduVGKY
Slides:
http://schd.ws/hosted_files/cppcon2016/0f/Wel‐
come%20To%20The%20Time%20Zone%20‐%20Howard%20Hinnant%20‐%20Cpp‐
Con%202016.pdf

"iso_week.h" is a header‐only library built on top
of the "date.h" library which implements the ISO week date calen‐
dar.
Documentation:  http://howardhinnant.github.io/date/iso_week.html

"julian.h"  is a header‐only library built on top of the "date.h"
library which implements a proleptic  Julian  calendar  which  is
fully interoperable with everything above.
Documentation:    http://howardhinnant.github.io/date/julian.html

"islamic.h" is a header‐only library built on top of the "date.h"
library  which  implements  a proleptic Islamic calendar which is
fully interoperable with everything above.
Documentation: http://howardhinnant.github.io/date/islamic.html


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
mkdir build && cd build
cmake -DENABLE_DATE_TESTING=on -DBUILD_TZ_LIB=on -DBUILD_SHARED_LIBS=on -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_CXX_FLAGS="$CXXFLAGS" -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS" ../
%make_build


%check


%install
cd build && %make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/lib%{system_name}-tz.so.3*


%files devel
%_includedir/%{system_name}/%{system_name}.h
%_includedir/%{system_name}/tz.h
%_libdir/lib%{system_name}-tz.so
%dir %_libdir/cmake/%{system_name}
%_libdir/cmake/%{system_name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
