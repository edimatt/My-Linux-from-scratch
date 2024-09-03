%global debug_package %{nil}
%define _build_id_links none
%define system_name gobject-introspection

Name:           EDO%{system_name}
Version:        1.80.1
Release:        1%{?dist}
Summary:        Describe the APIs and collect them in a uniform, machine readable format.
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.gnome.org/GNOME/gobject-introspection
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc EDOglib EDOlibffi-devel EDOlibiconv-devel EDOpcre2-devel
Requires:       glibc EDOgcc EDOglib EDOlibffi EDOlibiconv EDOpcre2
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
# BuildArch:      noarch
AutoReqProv:    no


%description
The goal of the project is to describe the APIs and collect them in
a uniform, machine readable format.


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
%_bindir/g-ir-*
%_mandir/man1/g-ir-*.1
%_libdir/libgirepository*.so.*


%files devel
%_includedir/%{system_name}*
%_libdir/%{system_name}/giscanner/*
%_libdir/girepository*
%_libdir/libgirepository*.so
%_libdir/pkgconfig/%{system_name}*.pc
%_datadir/gir*
%_datadir/%{system_name}*
%_datadir/aclocal/introspection.m4


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
