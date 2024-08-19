%global debug_package %{nil}
%define _build_id_links none
%define system_name setuptools

Name:           EDOpython-%{system_name}
Version:        72.2.0
Release:        1%{?dist}
Summary:        Easily download, build, install, upgrade, and uninstall Python packages.
License:        MIT 
URL:            https://%{system_name}.pypa.io
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no
BuildArch:      noarch


%description
Setuptools  is  a fully‐featured, actively‐maintained, and stable
library designed to facilitate packaging Python projects.

It helps developers to easily share reusable code (in the form of
a  library)  and  programs  (e.g.,  CLI/GUI  tools implemented in
Python), that can be installed with pip and uploaded to PyPI.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath


%install
%pip_install
# pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_bindir}/pip* %{buildroot}%{_libdir}


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_libdir}/python3.12/site-packages/%{system_name}*
%{_libdir}/python3.12/site-packages/pkg_resources/*
%{_libdir}/python3.12/site-packages/_distutils_hack/*
%{_libdir}/python3.12/site-packages/distutils-precedence.pth


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
