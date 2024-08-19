%global debug_package %{nil}
%define _build_id_links none
%define system_name alsa-lib

Name:           EDO%{system_name}
Version:        1.2.12
Release:        1%{?dist}
Summary:        Advanced Linux Sound Architecture (ALSA) project.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/alsa-project/alsa-lib
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc make
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The  alsa‐lib  is  a  library to interface with ALSA in the Linux
kernel and virtual devices using a plugin system.

The up‐to‐date reference generated from sources can  be  accessed
here:

http://www.alsa‐project.org/alsa‐doc/alsa‐lib/

You  may  give a look for more information about the ALSA project
to URL http://www.alsa‐project.org.


%description devel


%prep
%setup -n %{system_name}-%{version}
%autoreconf


%build
%set_build_flags_with_rpath
%_configure --disable-static
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/aserver
%_libdir/libasound.so.*
%_libdir/libatopology.so.*


%files devel
%_includedir/alsa/*
%_includedir/sys/asoundlib.h
%_includedir/asoundlib.h
%_datadir/alsa/*
%_datadir/aclocal/alsa.m4
%_libdir/libasound.so
%_libdir/libasound.la
%_libdir/libatopology.so
%_libdir/libatopology.la
%_libdir/pkgconfig/alsa*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
