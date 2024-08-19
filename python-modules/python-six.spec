%global debug_package %{nil}
%define _build_id_links none
%define system_name six

Name:           EDOpython-%{system_name}
Version:        1.16.0
Release:        1%{?dist}
Summary:        Python 2 and 3 compatibility utilities
License:        MIT 
URL:            https://pypi.org/project/%{system_name}/
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no
BuildArch:      noarch


%description
Six is a Python 2 and 3 compatibility library. It provides utili‐
ty functions for  smoothing  over  the  differences  between  the
Python versions with the goal of writing Python code that is com‐
patible on both Python versions. See the documentation  for  more
information on what is provided.

Six  supports  Python  2.7  and 3.3+. It is contained in only one
Python file, so it can be easily copied into your  project.  (The
copyright and license notice must be retained.)

Online documentation is at https://six.readthedocs.io/.

Bugs  can  be  reported  to https://github.com/benjaminp/six. The
code can also be found there.


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
%{_libdir}/python3.12/site-packages/__pycache__/%{system_name}.*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
