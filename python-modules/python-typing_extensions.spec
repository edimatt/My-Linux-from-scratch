%global debug_package %{nil}
%define _build_id_links none
%define system_name typing_extensions

Name:           EDOpython-%{system_name}
Version:        4.8.0
Release:        1%{?dist}
Summary:        Backported and Experimental Type Hints for Python 3.8+.
License:        MIT 
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
%{_libdir}/python3.11/site-packages/%{system_name}*
%{_libdir}/python3.11/site-packages/__pycache__/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
