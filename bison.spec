%global debug_package %{nil}
%define _build_id_links none
%define system_name bison

Name:           EDO%{system_name}
Version:        3.8.2
Release:        1%{?dist}
Summary:        A GNU general-purpose parser generator.
License:        GPL
URL:            https://www.gnu.org/software/bison
Source:         https://ftp.gnu.org/gnu/bison/%{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build glibc-devel
Requires:       glibc

AutoReqProv:    no

%description
Bison is a general purpose parser generator that converts a gram‐
mar description for an LALR(1) context‐free grammar into a C pro‐
gram  to  parse that grammar. Bison can be used to develop a wide
range of language parsers, from ones used in simple desk calcula‐
tors to complex programming languages. Bison is upwardly compati‐
ble with Yacc, so any correctly written Yacc grammar should  work
with  Bison  without any changes. If you know Yacc, you shouldn’t
have any trouble using Bison. You do need to be  very  proficient
in C programming to be able to use Bison. Bison is only needed on
systems that are used for development.  If your  system  will  be
used for C development, you should install Bison.


%prep
%setup -n %{system_name}-%{version}
%autoreconf


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name} --enable-threads=posix YFLAGS="-shared"
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING NEWS README THANKS TODO
%_bindir/%{system_name}
%_bindir/yacc
%_mandir/man1/%{system_name}.1
%_mandir/man1/yacc.1
%_libdir/liby.a
%ghost %_infodir/dir
%_infodir/%{system_name}.info*
%_datadir/%{system_name}/*
%_datadir/locale/*/LC_MESSAGES/%{system_name}*.mo
%_datadir/aclocal/%{system_name}*.m4
%_docdir/%{name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
