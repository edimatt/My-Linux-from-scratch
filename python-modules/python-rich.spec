%global debug_package %{nil}
%define _build_id_links none
%define system_name rich

Name:           EDOpython-%{system_name}
Version:        13.5.3
Release:        1%{?dist}
Summary:        Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal.
License:        MIT 
URL:            https://github.com/Textualize/rich
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython EDOpython-markdown-it-py EDOpython-Pygments < 3.0.0 EDOpython-Pygments >= 2.13.0
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
%{_libdir}/python3.12/site-packages/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
