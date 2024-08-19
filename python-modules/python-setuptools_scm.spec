%global debug_package %{nil}
%define _build_id_links none
%define system_name setuptools_scm

Name:           EDOpython-%{system_name}
Version:        8.1.0
Release:        1%{?dist}
Summary:        The blessed package to manage your versions by scm tags
License:        MIT 
URL:            https://%{system_name}.pypa.io
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython EDOpython-setuptools EDOpython-packaging
AutoReqProv:    no
BuildArch:      noarch


%description
setuptools‐scm  extracts  Python  package versions from git or hg
metadata instead of declaring them as the version argument or  in
an SCM managed file.

Additionally,  setuptools‐scm  provides setuptools with a list of
files that are managed by the SCM (i.e. it automatically adds all
of  the  SCM‐managed files to the sdist).  Unwanted files must be
excluded via MANIFEST.in.


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


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
