%global debug_package %{nil}
%define _build_id_links none
%define system_name nasm

Name:           EDO%{system_name}
Version:        2.16.01
Release:        1%{?dist}
Summary:        The Netwide Assembler.
License:        GPL
URL:            https://www.nasm.us
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build glibc-devel
Requires:       glibc
AutoReqProv:    no

%description
This  is the project webpage for the Netwide Assembler (NASM), an
asssembler for the x86 CPU architecture portable to nearly  every
modern  platform, and with code generation for many platforms old
and new.


%prep
%autosetup -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure
%make_build O="$O"


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%{system_name}
%_bindir/ndisasm
%_mandir/man1/%{system_name}.1
%_mandir/man1/ndisasm.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
