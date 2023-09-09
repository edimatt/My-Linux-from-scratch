%global debug_package %{nil}
%define _build_id_links none
%define system_name texinfo

Name:           EDO%{system_name}
Version:        7.0.3
Release:        1%{?dist}
Summary:        The official documentation format of the GNU project.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.gnu.org/software/texinfo
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOncurses-devel
Requires:       glibc EDOncurses-libs
Provides:       %{name} = %{version}


%description
Texinfo  uses  a single source file to produce output in a number
of formats, both online and printed (HTML, PDF, DVI,  Info,  Doc‐
Book,  LaTeX, EPUB 3). This means that instead of writing differ‐
ent documents for online information and another  for  a  printed
manual,  you  need write only one document. The Texinfo system is
well‐integrated with GNU Emacs.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure
%make_build


%check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*texi*
%_bindir/*info*
%_datadir/locale/*/LC_MESSAGES/%{system_name}*.mo
%_datadir/%{system_name}/*
%ghost %_infodir/dir
%_infodir/texi*
%_infodir/info*
%_mandir/man*/*info*
%_mandir/man*/*texi*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
