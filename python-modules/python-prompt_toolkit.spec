%global debug_package %{nil}
%define _build_id_links none
%define system_name prompt_toolkit

Name:           EDOpython-%{system_name}
Version:        3.0.47
Release:        1%{?dist}
Summary:        Library for building powerful interactive command lines in Python
License:        MIT 
URL:            https://pypi.org/project/%{system_name}/
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython EDOpython-wcwidth
AutoReqProv:    no
BuildArch:      noarch


%description
prompt_toolkit  is  a  library  for building powerful interactive
command line and terminal applications in Python.

It can be a very advanced pure Python replacement for  GNU  read‐
line,  but  it can also be used for building full screen applica‐
tions.


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
