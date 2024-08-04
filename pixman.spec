%global debug_package %{nil}
%define _build_id_links none
%define system_name pixman

Name:           EDO%{system_name}
Version:        0.43.4
Release:        1%{?dist}
Summary:        Pixman is a low-level software library for pixel manipulation.
License:        MIT
Vendor:         %{_vendor}
URL:            https://www.pixman.org/
Source0:        https://www.cairographics.org/releases/%{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc EDOpython-meson
Requires:       glibc EDOgcc
Provides:       %{name} = %{version}


%package devel
Summary:        Devel libraries and headers for %{system_name}.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Pixman  is  a  low‐level software library for pixel manipulation,
providing features such as image compositing and  trapezoid  ras‐
terization.  Important users of pixman are the cairo graphics li‐
brary and the X server.

Pixman is implemented as a library in the C programming language.
It runs on many platforms, including Linux, BSD Derivatives, Mac‐
OS X, and Windows.

Pixman is free and open source software. It is  available  to  be
redistributed and/or modified under the terms of the MIT license.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%meson_setup
%meson_build


%check
%meson_test


%install
%meson_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/lib%{system_name}-1.so.*


%files devel
%_libdir/lib%{system_name}-1.so
%_libdir/pkgconfig/%{system_name}-1.pc
%_includedir/%{system_name}-1/*.h


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
