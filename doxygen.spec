%global debug_package %{nil}
%global _lto_cflags %{nil}
%define _build_id_links none
%define system_name doxygen

Name:           EDO%{system_name}
Version:        1.11.0
Release:        1%{?dist}
Summary:        Documentation generator for C/C++.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/doxygen/doxygen
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc EDOzlib-devel EDOxapian-devel EDOsqlite-devel EDOspdlog-devel
Requires:       glibc EDOgcc EDOzlib EDOxapian EDOsqlite-libs EDOspdlog
Provides:       %{name} = %{version}


%description
Doxygen  is  the de facto standard tool for generating documenta‐
tion from annotated C++ sources, but it also supports other popu‐
lar  programming languages such as C, Objective‐C, C#, PHP, Java,
Python, IDL (Corba, Microsoft, and UNO/OpenOffice flavors),  For‐
tran,  and  to  some extent D. Doxygen also supports the hardware
description language VHDL.

Doxygen can help you in three ways:

It can generate an on‐line documentation browser (in HTML) and/or
an  off‐line reference manual (in LaTeX) from a set of documented
source files. There is also support for generating output in  RTF
(MS‐Word),  PostScript, hyperlinked PDF, compressed HTML, DocBook
and Unix man pages. The documentation is extracted directly  from
the sources, which makes it much easier to keep the documentation
consistent with the source code.  You can  configure  doxygen  to
extract  the  code structure from undocumented source files. This
is very useful to quickly find your way in large source distribu‐
tions. Doxygen can also visualize the relations between the vari‐
ous elements by means of include dependency  graphs,  inheritance
diagrams, and collaboration diagrams, which are all generated au‐
tomatically.  You can also use doxygen for creating normal  docu‐
mentation  (as I did for the doxygen user manual and doxygen web‐
site).


%prep
if rpm -q EDOlibiconv-devel; then
    echo "Remove libiconv devel before building %{system_name}."
    exit 1
fi
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%cmake_setup -DFLEX_INCLUDE_DIR=%_includedir -DICONV_INCLUDE_DIR=%_includedir -Duse_sys_spdlog=ON -Duse_sys_sqlite3=ON -Dbuild_doc=OFF -Dbuild_search=ON
%cmake_build


%check
# make check


%install
%cmake_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/doxy*
%_mandir/man1/doxy*.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
