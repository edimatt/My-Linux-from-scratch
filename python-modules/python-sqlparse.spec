%global debug_package %{nil}
%define _build_id_links none
%define system_name sqlparse

Name:           EDOpython-%{system_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        A non-validating SQL parser.
License:        MIT 
URL:            https://pypi.org/project/%{system_name}/
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no
BuildArch:      noarch


%description
sqlparse  is  a non‐validating SQL parser for Python. It provides
support for parsing, splitting and formatting SQL statements.

The module is compatible with Python 3.8+ and released under  the
terms of the New BSD license.

Visit  the  project  page at https://github.com/andialbrecht/sql‐
parse for further information about this project.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath


%install
%pip_install
pathfix.py -i %_bindir/python3 -n %buildroot%{python3_sitearch}/%{system_name}/cli.py


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_bindir}/sqlformat
%{_libdir}/python3.12/site-packages/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
