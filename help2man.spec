%global debug_package %{nil}
%define _build_id_links none
%define system_name help2man

Name:           EDO%{system_name}
Version:        1.49.3
Release:        1%{?dist}
Summary:        Produces manual pages from the ‘--help’ and ‘--version’ output of other commands. 
License:        GPL
URL:            https://www.gnu.org/software/help2man
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildArch:      noarch
BuildRequires:  rpm-build
Requires:       bash perl-interpreter
AutoReqProv:    no

%description
help2man  is  a  tool  for automatically generating simple manual
pages from program output.

Although  manual  pages  are  optional  for  GNU  programs  other
projects,  such as Debian require them (see Man Pages in GNU Cod‐
ing Standards)

This program is intended to provide an easy way for software  au‐
thors to include a manual page in their distribution without hav‐
ing to maintain that document.

Given a program which produces reasonably standard  '‐‐help'  and
'‐‐version'  outputs,  help2man  can  re‐arrange that output into
something which resembles a manual page.


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
%_mandir/man1/%{system_name}.1
%_infodir/%{system_name}.info


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
