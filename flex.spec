%global debug_package %{nil}
%define _build_id_links none
%define system_name flex

Name:           EDO%{system_name}
Version:        2.6.4
Release:        1%{?dist}
Summary:        Fast lexical analyzer generator.
License:        GPL
URL:            https://github.com/westes/flex
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOgcc
Requires:       glibc
AutoReqProv:    no


%description
The flex program generates scanners.  Scanners are programs which
can recognize lexical patterns in text.  Flex takes pairs of reg‐
ular  expressions  and  C  code as input and generates a C source
file as output.  The output file is compiled and  linked  with  a
library  to  produce  an  executable.   The  executable  searches
through its input for occurrences  of  the  regular  expressions.
When  a  match  is  found,  it executes the corresponding C code.
Flex was designed to work with both Yacc and Bison, and  is  used
by many programs as part of their build process.

You  should  install flex if you are going to use your system for
application development.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING NEWS ONEWS README.md
%_bindir/%{system_name}*
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo
%_bindir/%{system_name} 
%_mandir/man1/%{system_name}.1
%ghost %_infodir/dir
%_infodir/%{system_name}.info*
%_includedir/FlexLexer.h
%_libdir/libfl.*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
