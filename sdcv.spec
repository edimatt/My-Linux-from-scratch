%global debug_package %{nil}
%define _build_id_links none
%define system_name sdcv

Name:           EDO%{system_name}
Version:        0.5.5
Release:        1%{?dist}
Summary:        StarDict command line utility
License:        GPL-2
URL:            https://dushistov.github.io/sdcv/
Source:         %{system_name}-%{version}.tar.gz
Patch:          %{system_name}-%{version}-const.patch
BuildRequires:  rpm-build glibc-devel EDOgcc EDOglib-devel EDOlibiconv-devel EDOncurses-devel EDOpcre2-devel EDOreadline-devel EDOzlib-devel
Requires:       glibc EDOgcc EDOglib EDOlibiconv EDOncurses-libs EDOpcre2 EDOreadline EDOzlib
Provides:       %{name} = %{version}
AutoReqProv:    no


%description
sdcv  is a simple, cross‐platform, text‐based utility for working
with dictionaries in StarDict format.


%prep
%setup -n %{system_name}-%{version}
%patch -p1


%build
%set_build_flags_with_rpath
%cmake_setup
%cmake_build


%install
mkdir %_builddir/%{system_name}-%{version}/build/locale
%cmake_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1
%_mandir/uk/man1/%{system_name}.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
