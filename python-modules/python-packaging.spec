%global debug_package %{nil}
%define _build_id_links none
%define system_name packaging

Name:           EDOpython-%{system_name}
Version:        24.1
Release:        1%{?dist}
Summary:        Core utilities for Python packages
License:        MIT
URL:            https://%{system_name}.pypa.io
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no
BuildArch:      noarch


%description
Reusable  core  utilities for various Python Packaging interoper‐
ability specifications.

This library provides utilities that implement the interoperabil‐
ity  specifications which have clearly one correct behaviour (eg:
PEP 440) or benefit greatly from having a single shared implemen‐
tation (eg: PEP 425).

The  packaging  project includes the following: version handling,
specifiers, markers, requirements, tags, utilities.


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
