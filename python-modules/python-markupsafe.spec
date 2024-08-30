%global debug_package %{nil}
%define _build_id_links none
%define system_name MarkupSafe

Name:           EDOpython-%{system_name}
Version:        2.1.5
Release:        1%{?dist}
Summary:        Safely add untrusted strings to HTML/XML markup.
License:        BSDG
URL:            https://palletsprojects.com/p/markupsafe
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no


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
%{_libdir}/python3.12/site-packages/markupsafe/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
