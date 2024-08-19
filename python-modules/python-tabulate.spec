%global debug_package %{nil}
%define _build_id_links none
%define system_name tabulate

Name:           EDOpython-%{system_name}
Version:        0.9.0
Release:        1%{?dist}
Summary:        Pretty-print tabular data
License:        MIT
URL:            https://%{system_name}.github.io
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no
Buildarch:      noarch


%description
Pretty‐print tabular data in Python, a library and a command‐line
utility.

The main use cases of the library are:

printing small tables without hassle:  just  one  function  call,
formatting  is  guided  by the data itself authoring tabular data
for lightweight plain‐text markup: multiple output formats  suit‐
able  for further editing or transformation readable presentation
of mixed textual and numeric data: smart column  alignment,  con‐
figurable number formatting, alignment by a decimal point.


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
%_bindir/%{system_name}
%{_libdir}/python3.12/site-packages/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
