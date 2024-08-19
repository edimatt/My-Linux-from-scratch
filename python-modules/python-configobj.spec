%global debug_package %{nil}
%define _build_id_links none
%define system_name configobj

Name:           EDOpython-%{system_name}
Version:        5.0.8
Release:        1%{?dist}
Summary:        Config file reading, writing and validation
License:        MIT 
URL:            https://pypi.org/project/%{system_name}/
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython EDOpython-six
AutoReqProv:    no
BuildArch:      noarch


%description
ConfigObj is a simple but powerful config file reader and writer:
an ini file round tripper. Its main feature is that  it  is  very
easy  to use, with a straightforward programmerâs interface and a
simple syntax for config files.

List of Features: Nested sections  (subsections),  to  any  level
List  values Multiple line values Full Unicode support String in‐
terpolation (substitution) Integrated with a powerful  validation
system
 ‐ including automatic type checking/conversion
 ‐ and allowing default values
 ‐  repeated  sections All comments in the file are preserved The
order of keys/sections is  preserved  Powerful  unrepr  mode  for
storing/retrieving Python data‐types


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
%{_libdir}/python3.12/site-packages/validate/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
