%global debug_package %{nil}
%define _build_id_links none
%define system_name masker

Name:           EDOpython-%{system_name}
Version:        3.0.1
Release:        1%{?dist}
Summary:        A tool for masking files.
License:        Apache 2.0
URL:            https://masker.org
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build EDOgcc glibc-devel EDOpython
Requires:       glibc EDOpython EDOpython-msgpack EDOpython-typer EDOpython-tqdm
AutoReqProv:    no


%description
The masker is a tool for masking flat files.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath


%install
%pip_install
pathfix.py -i %_bindir/python3 -n %buildroot%_bindir/%{system_name}


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%{_libdir}/python3.12/site-packages/Masker*
%{_libdir}/python3.12/site-packages/%{system_name}*
# %{_mandir}/man1/%{system_name}.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
