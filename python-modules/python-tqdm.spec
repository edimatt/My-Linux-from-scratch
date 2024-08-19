%global debug_package %{nil}
%define _build_id_links none
%define system_name tqdm

Name:           EDOpython-%{system_name}
Version:        4.66.5
Release:        1%{?dist}
Summary:        A Fast, Extensible Progress Bar for Python and CLI
License:        Apache 2.0
URL:            https://tqdm.github.io
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no
BuildArch:      noarch


%description
tqdm  derives  from  the Arabic word taqaddum (ØªÙØ¯ÙÙ) which can
mean "progress," and is an abbreviation for "I love you so  much"
in Spanish (te quiero demasiado).

Instantly make your loops show a smart progress meter ‐ just wrap
any iterable with tqdm(iterable), and you’re done!


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
%{_libdir}/python3.12/site-packages/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
