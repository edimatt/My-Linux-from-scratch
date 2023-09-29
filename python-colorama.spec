%global debug_package %{nil}
%define _build_id_links none
%define system_name colorama

Name:           EDOpython-%{system_name}
Version:        0.4.6
Release:        1%{?dist}
Summary:        Cross-platform colored terminal text.
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


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
