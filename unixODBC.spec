%global debug_package %{nil}
%define _build_id_links none
%define system_name unixODBC

Name:           EDO%{system_name}
Version:        2.3.12
Release:        1%{?dist}
Summary:        Open Source ODBC sub-system and ODBC SDK.
License:        GPL
URL:            https://www.unixodbc.org/
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build glibc-devel EDOncurses-devel EDOreadline-devel EDOlibtool
Requires:       glibc EDOlibtool EDOncurses-libs EDOreadline
AutoReqProv:    no


%package devel
Summary:        Development tools.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The unixODBC Project goals are to develop and promote unixODBC to
be the definitive standard for ODBC on non MS Windows  platforms.
This  is  to include GUI support for both KDE and GNOME.  ODBC is
an open specification for providing application developers with a
predictable  API  with which to access Data Sources. Data Sources
include SQL Servers and any Data Source with an ODBC Driver.

The two major advantages of choosing to code  an  application  to
the ODBC API are:

‐  Portable Data Access Code: The ODBC API, as outlined by X/Open
and ISO, is availible on all major platforms. Microsoft platforms
include  many  enhancements to this specification; these enhance‐
ments are also supported by unixODBC

‐ Dynamic Data Binding: This allows the user or the system admin‐
istrator  to easily configure an application to use any ODBC com‐
pliant data source. This is perhaps the single biggest  advantage
of  coding  an  application to the ODBC API and to purchase these
applications. Dyamic binding allows the end‐user to pick  a  data
source,  ie  an  SQL Server, and use it for all data applications
without having to worry about recompiling the application.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure
%make_build


%install
%make_install


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*
%_mandir/man1/*.1
%_mandir/man5/odbc*.ini.5
%_mandir/man7/%{system_name}.7
%_libdir/libodbc*.so.2*
%_sysconfdir/odbc*.ini

%files devel
%_libdir/libodbc*.so
%_libdir/libodbc*.la
%_libdir/pkgconfig/odbc*.pc
%_includedir/%{system_name}/unixodbc_conf.h
%_includedir/*.h


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
