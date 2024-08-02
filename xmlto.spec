%global debug_package %{nil}
%define _build_id_links none
%define system_name xmlto

Name:           EDO%{system_name}
Version:        0.0.29
Release:        1%{?dist}
Summary:        A tool for converting XML files to various formats
License:        GPL
URL:            https://pagure.io/xmlto
Source0:        https://pagure.io/xmlto/releases/%{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build make glibc-devel EDOgcc
Requires:       bash glibc
AutoReqProv:    no


%description
Utility  xmlto  is a simple shell script for converting XML files
to various formats. It  serves  as  an  easy‐to‐use  command‐line
frontend  to  make  fine output without remembering many long op‐
tions and searching for the syntax of the backends.

Currently, it supports conversion from docbook,  xhtml1,  and  fo
format  to  various  output formats (awt, fo, htmlhelp, javahelp,
mif, pdf, svg, xhtml, dvi, html,  html‐nochunks,  man,  pcl,  ps,
txt,  xhtml‐nochunks).  Some output formats may be unavailable if
you don’t have all prerequisites installed, as xmlto  uses  back‐
ends (xsltproc, passivetex/fop/dblatex) for processing.

You could check and generate the offline version of documentation
with xmlto from doc/xmlif.xml sources. However, if  you  received
the  xmlif as a part of the distribution, you should already have
the xmlif(1) manpage on your machine.

If you received xmlto as a part of the distribution,  you  should
already have the xmlto(1) manpage on your machine.


%prep
%setup -n %{system_name}-%{version}
%autoreconf


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
%_bindir/xmlif
%_mandir/man1/%{system_name}.1
%_mandir/man1/xmlif.1
%_datadir/%{system_name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
