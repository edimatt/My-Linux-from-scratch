%global debug_package %{nil}
%define _build_id_links none
%define system_name sed

Name:           EDO%{system_name}
Version:        4.9
Release:        1%{?dist}
Summary:        A GNU stream text editor.
License:        GPL
URL:            https://www.gnu.org/software/sed
Source:         https://ftp.gnu.org/gnu/sed/%{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build glibc-devel
Requires:       glibc
AutoReqProv:    no

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.


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
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
