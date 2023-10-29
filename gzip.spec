%global debug_package %{nil}
%define _build_id_links none
%define system_name gzip

Name:           EDO%{system_name}
Version:        1.13
Release:        1%{?dist}
Summary:        The GNU data compression program.
License:        GPL
URL:            https://www.gnu.org/software/gzip
Source:         https://ftp.gnu.org/gnu/gzip/%{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build glibc-devel
Requires:       glibc
AutoReqProv:    no

%description
The  gzip  package contains the popular GNU gzip data compression
program. Gzipped files have a .gz extension.
Gzip should be installed on your system, because  it  is  a  very
commonly used data compression program.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure
%make_build


%install
%make_install
%__rm %{buildroot}%{_bindir}/uncompress


%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/z*
%_bindir/g*
%_mandir/man1/g*.1
%_mandir/man1/z*.1
%ghost %_infodir/dir
%_infodir/%{system_name}.info


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
