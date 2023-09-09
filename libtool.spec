%global debug_package %{nil}
%define _build_id_links none
%define system_name libtool

Name:           EDO%{system_name}
Version:        2.4.7
Release:        1%{?dist}
Summary:        The GNU Portable Library Tool.
License:        GPL
URL:            https://www.gnu.org/software/libtool
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel rpm-build EDOhelp2man
Requires:       glibc bash
AutoReqProv:    no

%description
GNU Libtool is a set of shell scripts which automatically config‐
ure UNIX and UNIX‐like systems to generically  build  shared  li‐
braries.  Libtool provides a consistent, portable interface which
simplifies the process of using shared libraries.

If you are developing programs which will use  shared  libraries,
but  do  not use the rest of the GNU Autotools (such as GNU Auto‐
conf and GNU Automake), you should install the libtool package.

The libtool package also includes all files needed  to  integrate
the  GNU  Portable Library Tool (libtool) and the GNU Libtool Dy‐
namic Module Loader (ltdl) into a package built using the GNU Au‐
totools (including GNU Autoconf and GNU Automake).


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}*
%_mandir/man1/%{system_name}*.1
%_libdir/libltdl.*
%_includedir/ltdl.h
%_includedir/libltdl/*.h
%_datadir/aclocal/*.m4
%_datadir/%{system_name}/*
%ghost %_infodir
%_infodir/%{system_name}.info*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
