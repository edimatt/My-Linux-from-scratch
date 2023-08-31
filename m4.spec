%global debug_package %{nil}
%define _build_id_links none
%define system_name m4

Name:           EDO%{system_name}
Version:        1.4.19
Release:        1%{?dist}
Summary:        GNU macro processor.
License:        GPL
URL:            https://www.gnu.org/software/m4/
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build
Requires:       bash
AutoReqProv:    no

%description
A GNU implementation of the traditional UNIX macro processor.  M4
is useful for writing text files which can be  logically  parsed,
and  is used by many programs as part of their build process.  M4
has built‐in functions for including files,  running  shell  com‐
mands,  doing arithmetic, etc.  The autoconf program needs m4 for
generating configure  scripts,  but  not  for  running  configure
scripts.

Install m4 if you need a macro processor.


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
%_bindir/%{system_name}
%ghost %_infodir/dir
%_infodir/%{system_name}.info*
%_mandir/man1/%{system_name}.1
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
