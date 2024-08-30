%global debug_package %{nil}
%define _build_id_links none
%define system_name pygments

Name:           EDOpython-%{system_name}
Version:        2.18.0
Release:        1%{?dist}
Summary:        Pygments is a syntax highlighting package written in Python.
License:        BSD-2
URL:            https://pip.pypa.io
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
%{_bindir}/pygmentize
%{_libdir}/python3.12/site-packages/pygments/*
%{_libdir}/python3.12/site-packages/%{system_name}-%{version}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
