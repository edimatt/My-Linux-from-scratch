%global debug_package %{nil}
%define _build_id_links none
%define system_name pkgconf

Name:           EDO%{system_name}
Version:        2.0.2
Release:        1%{?dist}
Summary:        Configure compiler and linker flags for development frameworks.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/pkgconf/pkgconf
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOautoconf >= 2.71
Requires:       glibc
Provides:       %{name} = %{version}


%description
pkgconf is a program which helps to configure compiler and linker
flags for development libraries. It is similar to pkg‐config from
freedesktop.org.

libpkgconf  is  a  library  which provides access to most of pkg‐
conf’s functionality, to allow other tooling  such  as  compilers
and IDEs to discover and use libraries configured by pkgconf.


%prep
%setup -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure --disable-static
%make_build


%check
# Requires the kyua framework.
# make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%_bindir/bomtool
%_libdir/lib%{system_name}.so*
%_libdir/lib%{system_name}.la
%_libdir/pkgconfig/lib%{system_name}.pc
%_includedir/%{system_name}/*
%_mandir/man1/%{system_name}.1
%_mandir/man5/*
%_mandir/man7/pkg.m4.7
%_docdir/%{system_name}/*
%_datadir/aclocal/pkg.m4


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
