%global debug_package %{nil}
%define _build_id_links none
%define system_name gsettings-desktop-schemas

Name:           EDO%{system_name}
Version:        47
Release:        1%{?dist}
Summary:        Collection of GSettings schemas
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}
BuildArch:      noarch


%description
gsettings-desktop-schemas contains a collection of GSettings schemas for
settings shared by various components of a desktop.
You may download updates to the package from:
https://download.gnome.org/sources/gsettings-desktop-schemas/
To discuss gsettings-desktop-schemas, you may use the GNOME forum:
https://discourse.gnome.org/c/platform/


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
%_datadir/glib*
%_datadir/gir-1.0/GDesktopEnums-3.0.gir
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo
%_datadir/pkgconfig/%{system_name}.pc
%_datadir/GConf/*
%_libdir/girepository*
%_includedir/%{system_name}/gdesktop-enums.h


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
