%global debug_package %{nil}
%define _build_id_links none
%define system_name shellingham

Name:           EDOpython-%{system_name}
Version:        1.5.3
Release:        1%{?dist}
Summary:        Tool to Detect Surrounding Shell.
License:        ISC
URL:            https://github.com/sarugaku/shellingham
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
