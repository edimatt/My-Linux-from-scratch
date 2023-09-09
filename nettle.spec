%global debug_package %{nil}
%define _build_id_links none
%define system_name nettle

Name:           EDO%{system_name}
Version:        3.9.1
Release:        1%{?dist}
Summary:        A low-level cryptographic library.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.lysator.liu.se/~nisse/nettle/
Source0:        %{system_name}-%{version}.tar.gz
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
Nettle  is a cryptographic library that is designed to fit easily
in more or less any context: In crypto toolkits  for  object‐ori‐
ented  languages  (C++,  Python, Pike, ...), in applications like
LSH or GNUPG, or even in kernel space. In most contexts, you need
more  than the basic cryptographic algorithms, you also need some
way to keep track of available algorithms, their  properties  and
variants.  You often have some algorithm selection process, often
dictated by a protocol you want to implement.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --disable-static   
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}-*
%_bindir/*-conv
%_libdir/lib%{system_name}*.so.8*
%_libdir/libhogweed.so.6*


%files devel
%_includedir/%{system_name}/*.h
%_libdir/lib%{system_name}*.so
%_libdir/libhogweed.so
%_libdir/pkgconfig/%{system_name}*.pc
%_libdir/pkgconfig/hogweed.pc
%ghost %_infodir/dir
%_infodir/%{system_name}.info

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
