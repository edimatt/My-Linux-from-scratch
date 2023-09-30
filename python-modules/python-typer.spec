%global debug_package %{nil}
%define _build_id_links none
%define system_name typer

Name:           EDOpython-%{system_name}
Version:        0.9.0
Release:        1%{?dist}
Summary:        Typer, build great CLIs. Easy to code. Based on Python type hints.
License:        GPL
URL:            https://github.com/tiangolo/typer
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython EDOpython-typing_extensions EDOpython-click
AutoReqProv:    no
BuildArch:      noarch


%description


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath


%install
%pip_install


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_libdir}/python3.11/site-packages/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
