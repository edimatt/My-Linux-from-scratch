%global debug_package %{nil}
%define _build_id_links none
%define system_name markdown-it-py

Name:           EDOpython-%{system_name}
Version:        3.0.0
Release:        1%{?dist}
Summary:        Python port of markdown-it. Markdown parsing, done right!
License:        MIT 
URL:            https://pip.pypa.io
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython EDOpython-mdurl
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
%{_bindir}/markdown-it
%{_libdir}/python3.11/site-packages/markdown_it*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
