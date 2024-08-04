%global debug_package %{nil}
%define _build_id_links none
%define system_name fontconfig

Name:           EDO%{system_name}
Version:        2.15.0
Release:        1%{?dist}
Summary:        Library for configuring and customizing font access.
License:        MIT
Vendor:         %{_vendor}
URL:            https://www.freedesktop.org/wiki/Software/fontconfig/
Source0:        %{system_name}-%{version}.tar.gz
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
Fontconfig can:
discover  new fonts when installed automatically, removing a com‐
mon source of configuration problems.  Perform font name  substi‐
tution,  so that appropriate alternative fonts can be selected if
fonts are missing.  Identify the set of fonts  required  to  com‐
pletely  cover  a set of languages.  Have GUI configuration tools
built as it uses an XML‐based configuration file (though with au‐
todiscovery, we believe this need is minimized).  Efficiently and
quickly find the fonts you need among the set of fonts  you  have
installed,  even  if you have installed thousands of fonts, while
minimzing memory usage.  Be used in concert with the X Render Ex‐
tension  and FreeType to implement high quality, anti‐aliased and
subpixel rendered text on a display.

Fontconfig does not:
render the fonts themselves (this is left to  FreeType  or  other
rendering mechanisms). Depend on the X Window System in any fash‐
ion, so that printer only applications do not have such dependen‐
cies.


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
%_bindir/fc-*
%_libdir/lib%{system_name}.so.*
%_datadir/xml/fontconfig/fonts.dtd
%_sysconfdir/fonts/*


%files devel
%_libdir/lib%{system_name}.so
%_libdir/pkgconfig/%{system_name}.pc
%_includedir/%{system_name}/*.h
%_datadir/%{system_name}/*
%_datadir/locale/*/LC_MESSAGES/fontconfig*.mo
%_datadir/gettext/its/fontconfig.*



%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
