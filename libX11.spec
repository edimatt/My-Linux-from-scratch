%global debug_package %{nil}
%define _build_id_links none
%define system_name libX11

Name:           EDO%{system_name}
Version:        1.8.7
Release:        1%{?dist}
Summary:        libX11 - Core X11 protocol client library
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/lib/libx11
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros EDOxtrans EDOxproto EDOxextproto EDOlibxcb-devel EDOinputproto EDOkbproto EDOlibxcb-devel EDOlibXau-devel
Requires:       glibc EDOlibxcb EDOlibXau
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
%_datadir/X11/*
%_libdir/%{system_name}*.so.*


%files devel
%_includedir/X11/*
%_mandir/man3/*.3
%_mandir/man5/*Compose.5
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/x11*.pc
%_docdir/%{name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
