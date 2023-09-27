%global debug_package %{nil}
%define _build_id_links none
%define system_name bc

Name:           EDO%{system_name}
Version:        1.07
Release:        1%{?dist}
Summary:        A binary calculator.
License:        GPL
URL:            https://github.com/gavinhoward/bc
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOreadline-devel EDOncurses-devel
Requires:       glibc EDOreadline EDOncurses-libs
AutoReqProv:    no


%description
bc  is an arbitrary precision numeric processing language. Syntax
is similar to C, but differs in many substantial areas.  It  sup‐
ports  interactive  execution  of statements. bc is a utility in‐
cluded in the POSIX P1003.2/D11 draft standard.

Since the POSIX document does not specify how bc must  be  imple‐
mented, this version does not use the historical method of having
bc be a compiler for the dc calculator. This version has a single
executable that both compiles the language and runs the resulting
byte code. The byte code is not the dc language.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --with-readline
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING NEWS README
%_bindir/%{system_name}
%_bindir/dc
%_mandir/man1/%{system_name}.1
%_mandir/man1/dc.1
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_infodir/dc.info


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
