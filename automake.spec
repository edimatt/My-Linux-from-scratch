%global debug_package %{nil}
%define _build_id_links none
%define system_name automake

Name:           EDO%{system_name}
Version:        1.16
Release:        1%{?dist}
Summary:        A GNU tool for automatically creating Makefiles.
License:        GPL
URL:            https://www.gnu.org/software/automake
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildArch:      noarch
BuildRequires:  rpm-build
Requires:       bash
AutoReqProv:    no

%description
GNU Automake is a tool for automatically generating Makefile.in
files compliant with the GNU Coding Standards.


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
%_bindir/auto*
%_bindir/aclocal*
%_datadir/%{system_name}-%{version}/*
%_datadir/aclocal-%{version}/*
%_datadir/aclocal/README
%_docdir/%{system_name}/*
%ghost %_infodir/dir
%_infodir/%{system_name}*
%_mandir/man1/auto*.1
%_mandir/man1/aclocal*.1



%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
