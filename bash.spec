%global debug_package %{nil}
%define _build_id_links none
%define system_name bash

Name:           EDO%{system_name}
Version:        5.2.15
Release:        1%{?dist}
Summary:        The Bourne Again SHell.
License:        GPL
URL:            https://www.gnu.org/software/bash
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build EDOncurses-devel EDOlibiconv-devel
Requires:       glibc EDOncurses-libs EDOlibiconv
AutoReqProv:    no

%description
Bash  is  the GNU Project’s shellâthe Bourne Again SHell. This is
an sh‐compatible shell that incorporates useful features from the
Korn shell (ksh) and the C shell (csh). It is intended to conform
to the IEEE POSIX P1003.2/ISO 9945.2 Shell and Tools standard. It
offers  functional  improvements over sh for both programming and
interactive use. In addition, most sh scripts can be run by  Bash
without modification.

The improvements offered by Bash include:

    command‐line editing,
    unlimited size command history,
    job control,
    shell functions and aliases,
    indexed arrays of unlimited size,
    integer arithmetic in any base from two to sixty‐four.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --enable-readline --enable-threads=posix --enable-profiling --enable-select --enable-progcomp --enable-multibyte --enable-job-control --enable-history --enable-help-builtin --enable-directory-stack --enable-dparen-arithmetic --enable-extended-glob --enable-cond-command --enable-cond-regexp --enable-coprocesses --enable-debugger --enable-array-variables --enable-alias --enable-brace-expansion --enable-casemod-attributes --enable-casemod-expansions --without-bash-malloc --docdir=%_docdir/%{name}
%make_build


%install
%make_install
cd %{buildroot}%{_bindir} && ln -sfv %{system_name} sh && cd -


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc CHANGES COMPAT NEWS POSIX RBASH README FAQ INTRO bash.html bashref.html
%_bindir/sh
%_bindir/%{system_name}*
%_mandir/man1/%{system_name}*.1
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo
%_libdir/%{system_name}/*
%_libdir/pkgconfig/%{system_name}.pc
%_includedir/%{system_name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
