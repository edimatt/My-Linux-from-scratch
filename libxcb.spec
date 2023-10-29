%global debug_package %{nil}
%define _build_id_links none
%define system_name libxcb

Name:           EDO%{system_name}
Version:        1.15
Release:        1%{?dist}
Summary:        X Protocol Extensions.
License:        GPL
Vendor:         %{_vendor}
URL:            https://xcb.freedesktop.org
Source0:        https://xcb.freedesktop.org/dist/%{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros EDOxcb-proto EDOlibXau-devel
Requires:       glibc EDOlibXau
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description


%description devel


%prep
%setup -q -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/libxcb*.so.*


%files devel
%_docdir/%{name}/*
%_includedir/xcb/*.h
%_mandir/man3/xcb*.3
%_libdir/libxcb*.so
%_libdir/libxcb*.la
%_libdir/pkgconfig/xcb*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
