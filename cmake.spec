%global debug_package %{nil}
%define _build_id_links none
%define system_name cmake

Name:           EDO%{system_name}
Version:        3.30.1
Release:        1%{?dist}
Summary:        A Powerful Software Build System
License:        BSD
Vendor:         %{_vendor}
URL:            https://cmake.org/
Source0:        %{system_name}-%{version}.tar.gz
Patch0:         %{system_name}-%{version}-vimfiles.patch
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc EDOlibiconv-devel EDOlibidn2-devel EDOlibunistring-devel EDOncurses-devel EDOopenssl-devel
Requires:       glibc EDOgcc EDOlibiconv EDOlibidn2 EDOlibunistring EDOncurses-libs EDOopenssl-libs

Provides:       %{name} = %{version}


%description
CMake  is  a  cross‐platform, open‐source build system generator.
For full documentation visit the CMake Home Page  and  the  CMake
Documentation Page. The CMake Community Wiki also references use‐
ful guides and recipes.
CMake is maintained and supported by  Kitware  and  developed  in
collaboration with a productive community of contributors.


%prep
%setup -q -n %{system_name}-%{version}
%patch0 -p1


%build
%set_build_flags_with_rpath
./bootstrap --prefix=%_prefix --docdir=share/doc/%{name}
%make_build


%check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/c*
%_docdir/%{name}/*
%_datadir/%{system_name}*
%_datadir/vim/*
%_datadir/emacs/site-lisp/%{system_name}-mode.el
%_datadir/aclocal/%{system_name}.m4
%_datadir/bash-completion/completions/c*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
