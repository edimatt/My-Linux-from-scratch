%global debug_package %{nil}
%define _build_id_links none
%define system_name glib

Name:           EDO%{system_name}
Version:        2.78.0
Release:        1%{?dist}
Summary:        A library of handy utility functions.
License:        GPL
Vendor:         %{_vendor}
URL:            https://download.gnome.org/sources/glib/2.78/
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc EDOlibffi-devel EDOpcre2-devel EDOutil-linux-devel EDOzlib-devel EDOzstd-devel
Requires:       glibc EDOgcc EDOlibffi EDOpcre2 EDOutil-linux EDOzlib EDOzstd
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
AutoReqProv:    no


%description
GLib  is  the  low‐level  core  library  that forms the basis for
projects such as GTK+ and GNOME. It provides data structure  han‐
dling  for  C, portability wrappers, and interfaces for such run‐
time functionality as an event loop,  threads,  dynamic  loading,
and an object system.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%meson_setup
%ninja_build


%check


%install
%ninja_install
for script in $(find %{buildroot}%{_datadir}/gdb -type f -name '*.py')
do
    %__mv $script %{buildroot}%{_datadir}/%{system_name}-2.0/
done


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/gapplication
%_bindir/gdbus
%_bindir/gio
%_bindir/gio-querymodules
%_bindir/glib-compile-schemas
%_bindir/gsettings
%_datadir/bash-completion/*
%_datadir/locale/*/LC_MESSAGES/%{system_name}20.mo
%_libdir/libg*.so.0*


%files devel
%_bindir/gdbus-codegen
%_bindir/glib-compile-resources
%_bindir/glib-ge*
%_bindir/glib-mkenums
%_bindir/gresource
%_bindir/gtester*
%_bindir/gobject-query
%_includedir/%{system_name}-*
%_includedir/gio-unix*
%_datadir/%{system_name}-*
%_datadir/gettext/*
%_datadir/aclocal/*
%_libdir/gio-launch-desktop
%_libdir/libg*.so
%_libdir/%{system_name}-2.0/*
%_libdir/pkgconfig/*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
