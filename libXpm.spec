%global debug_package %{nil}
%define _build_id_links none
%define system_name libXpm

Name:           EDO%{system_name}
Version:        3.5.15
Release:        1%{?dist}
Summary:        X Pixmap (XPM) image file format library.
License:        GPL
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/lib/libxpm
Source0:        https://gitlab.freedesktop.org/xorg/lib/libxpm/-/tags/%{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros EDOncompress EDOlibX11-devel EDOlibxcb-devel EDOlibXau-devel EDOxproto EDOxextproto EDOglib-devel
Requires:       glibc EDOlibX11 EDOlibxcb EDOlibXau EDOglib
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
%_configure --docdir=%_docdir/%{name} --disable-stat-zfile
%make_build


%check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/cxpm
%_mandir/man1/*xpm.1
%_libdir/%{system_name}.so.*


%files devel
%_includedir/X11/*
%_mandir/man3/Xpm*.3
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/xpm.pc

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
