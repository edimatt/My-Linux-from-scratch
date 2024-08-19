%global debug_package %{nil}
%define _build_id_links none
%define system_name litecli

Name:           EDOpython-%{system_name}
Version:        1.11.0
Release:        1%{?dist}
Summary:        CLI for SQLite Databases with auto-completion and syntax highlighting.
License:        Apache 2.0
URL:            https://%{system_name}.github.io
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build EDOpython
Requires:       glibc EDOpython EDOpython-sqlparse EDOpython-prompt_toolkit EDOpython-cli_helpers EDOpython-pygments EDOpython-click
AutoReqProv:    no
BuildArch:      noarch


%description


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath


%install
%pip_install
pathfix.py -i %_bindir/python3 -n %buildroot%_bindir/%{system_name}


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%{_libdir}/python3.12/site-packages/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
