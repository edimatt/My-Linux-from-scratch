%global debug_package %{nil}
%define _build_id_links none
%define system_name jansson

Name:           EDO%{system_name}
Version:        2.14
Release:        1%{?dist}
Summary:        Jansson is a C library for encoding, decoding and manipulating JSON data.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/akheron/jansson
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
Jansson  is  a  C library for encoding, decoding and manipulating
JSON data. Its main features and design principles are:

    Simple and intuitive API and data model
    Comprehensive documentation
    No dependencies on other libraries
    Full Unicode support (UTF‐8)
    Extensive test suite

Jansson is licensed under the MIT license;  see  LICENSE  in  the
source distribution for details.


%description devel


%prep
%setup -n %{system_name}-%{version}
autoreconf -fi


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
%_libdir/lib%{system_name}.so.4*
%_libdir/lib%{system_name}.a


%files devel
%_includedir/%{system_name}*.h
%_libdir/pkgconfig/%{system_name}.pc
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}.la


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
