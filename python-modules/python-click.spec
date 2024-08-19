%global debug_package %{nil}
%define _build_id_links none
%define system_name click

Name:           EDOpython-%{system_name}
Version:        8.1.7
Release:        1%{?dist}
Summary:        Composable command line interface toolkit.
License:        BSD-3
URL:            https://palletsprojects.com/p/click
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython
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
%{_libdir}/python3.12/site-packages/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
