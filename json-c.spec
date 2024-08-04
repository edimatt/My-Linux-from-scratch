%global debug_package %{nil}
%define _build_id_links none
%define system_name json-c

Name:           EDO%{system_name}
Version:        0.17
Release:        1%{?dist}
Summary:        JSON implementation in C
License:        MIT
URL:            https://github.com/json-c/json-c
Source0:        %{system_name}-%{version}.tar.xz
BuildRequires:  glibc-devel EDOgcc EDOcmake make
Requires:       glibc EDOgcc
Provides:       %{name} = %{version}
AutoReqProv:    no


%package devel
Summary:        Devel libraries and headers for %{system_name}.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
JSON‐C  implements  a reference counting object model that allows
you to easily construct JSON objects in C, output  them  as  JSON
formatted  strings and parse JSON formatted strings back into the
C representation of JSON objects. It aims to conform to RFC 8259.

Skip down to Using json‐c or check out the API docs, if  you  al‐
ready have json‐c installed and ready to use.

Home page for json‐c: https://github.com/json‐c/json‐c/wiki


%description devel
Headers and development files for linbrary %{system_name}.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%cmake_setup 
cd build && %make_build


%install
cd build && %make_install


%clean
rm -rf $RPM_BUILD_ROOT


%check
cd build && make test


%files
%_libdir/lib%{system_name}.so.*


%files devel
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}.a
%_libdir/cmake/%{system_name}/*.cmake
%_libdir/pkgconfig/%{system_name}.pc
%_includedir/%{system_name}/*.h


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
