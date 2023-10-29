%global debug_package %{nil}
%define _build_id_links none
%define system_name libutempter

Name:           EDO%{system_name}
Version:        1.2.2
Release:        1%{?dist}
Summary:        A privileged helper for utmp/wtmp updates.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/altlinux/libutempter
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
This  library  provides  interface for terminal emulators such as
screen and xterm to record user sessions to utmp and wtmp files.


%description devel
This package contains the header files and libraries for develop‐
ing with %{system_name}.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
cd %{system_name} && %{make_build}


%check


%install
cd %{system_name} && %{make_install} libdir=%_libdir libexecdir=%_libexecdir includedir=%_includedir mandir=%_mandir man3dir=%_mandir/man3


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc README
%_libexecdir/utempter/utempter
%_libdir/%{system_name}*.so.*


%files devel
%_mandir/man3/*
%_includedir/utempter.h
%_libdir/%{system_name}*.so


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
