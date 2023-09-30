%global debug_package %{nil}
%define _build_id_links none
%define system_name dejagnu

Name:           EDO%{system_name}
Version:        1.6.3
Release:        1%{?dist}
Summary:        GNU Test framework
License:        GPL
URL:            https://www.gnu.org/software/dejagnu
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOgcc EDOexpect
Requires:       glibc EDOexpect
AutoReqProv:    no
BuildArch:      noarch


%description
DejaGnu is a framework for testing other programs. Its purpose is
to provide a single front end for all tests. Think  of  it  as  a
custom  library  of  Tcl  procedures crafted to support writing a
test harness. A test harness is the testing  infrastructure  that
is  created  to  support a specific program or tool. Each program
can have multiple testsuites, all supported by a single test har‐
ness.  DejaGnu  is  written  in Expect, which in turn uses Tcl ‐‐
Tool command language.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
mkdir _build && cd _build
%_prev_configure
%make_build


%install
cd _build && %make_install


%check
cd _build && make check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%_bindir/runtest
%_mandir/man1/%{system_name}*.1
%_mandir/man1/runtest.1
%_datadir/%{system_name}/*
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_includedir/%{system_name}.h



%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
