%global debug_package %{nil}
%global isolated_build 1
%define _build_id_links none
%define system_name pip

Name:           EDOpython-%{system_name}
Version:        23.2.1
Release:        1%{?dist}
Summary:        The PyPA recommended tool for installing Python packages.
License:        MIT 
URL:            https://pip.pypa.io
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no
BuildArch:      noarch


%description
pip  is  the  package installer for Python. You can use it to in‐
stall packages from the Python Package Index and other indexes.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath


%install
%pip_install
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_bindir}/pip* %{buildroot}%{_libdir}


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}*
%{_libdir}/python3.11/site-packages/%{system_name}*
# %{_mandir}/man1/%{system_name}.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
