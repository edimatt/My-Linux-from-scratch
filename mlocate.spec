%global debug_package %{nil}
%define _build_id_links none
%define system_name mlocate

Name:           EDO%{system_name}
Version:        0.26
Release:        1%{?dist}
Summary:        An utility for finding files by name.
License:        GPL
URL:            https://fossies.org/linux/privat/old
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build
Requires:       glibc
AutoReqProv:    no

%description
mlocate is a locate/updatedb implementation.  It keeps a database
of all existing files and allows you to lookup files by name.

The ’m’ stands for "merging": updatedb reuses the existing  data‐
base  to avoid rereading most of the file system, which makes up‐
datedb faster and does not trash the system  caches  as  much  as
traditional locate implementations.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --with-libiconv-prefix=%_prefix --with-libintl-prefix=%_prefix
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/locate
%_bindir/updatedb
%_mandir/man1/locate.1
%_mandir/man5/*db*.5
%_mandir/man8/updatedb.8
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
