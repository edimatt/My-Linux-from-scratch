%global debug_package %{nil}
%define _build_id_links none
%define system_name cairo

Name:           EDO%{system_name}
Version:        1.18.0
Release:        1%{?dist}
Summary:        A 2D graphics library
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.cairographics.org/
Source0:        https://www.cairographics.org/releases/%{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc make EDOjson-c-devel EDOpixman-devel EDOfreetype-devel EDOfontconfig-devel
Requires:       glibc EDOgcc EDOjson-c EDOpixman EDOfreetype EDOfontconfig
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Cairo  is  a 2D graphics library designed to provide high‐quality
display and print output. Currently supported output targets  in‐
clude  the  X  Window  System, in‐memory image buffers, and image
files (PDF, PostScript, and SVG).

Cairo is designed to produce consistent output on all output  me‐
dia  while taking advantage of display hardware acceleration when
available.


%description devel
Cairo  is  a 2D graphics library designed to provide high‐quality
display and print output.

This package contains libraries, header files and developer docu‐
mentation  needed  for  developing  software which uses the cairo
graphics library.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%meson_setup --buildtype=release
%ninja_build


%check


%install
%ninja_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}-trace
%_libdir/%{system_name}/*.so
%_libdir/lib%{system_name}*.so.*


%files devel
%_includedir/%{system_name}/*
%_libdir/pkgconfig/%{system_name}*.pc
%_libdir/lib%{system_name}*.so


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
