%global debug_package %{nil}
%define _build_id_links none
%define system_name make

Name:           EDO%{system_name}
Version:        4.4
Release:        1%{?dist}
Summary:        A GNU tool which simplifies the build process for users.
License:        GPL
URL:            https://www.gnu.org/software/make
Source:         https://ftp.gnu.org/gnu/make/%{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel
Requires:       glibc
AutoReqProv:    no

%description
A GNU tool for controlling the generation of executables and oth‐
er non‐source files of a program from the program’s source files.
Make  allows users to build and install packages without any sig‐
nificant knowledge about the details of the  build  process.  The
details  about  how  the program should be built are provided for
make in the program’s


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1
%_includedir/gnu%{system_name}.h
%ghost %_infodir/dir
%_infodir/%{system_name}.info*
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo



%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
