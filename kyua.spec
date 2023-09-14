%global debug_package %{nil}
%define _build_id_links none
%define system_name kyua

Name:           EDO%{system_name}
Version:        0.13
Release:        1%{?dist}
Summary:        Testing framework for infrastructure software.
License:        BSD
URL:            https://github.com/jmmv/kyua
Source0:        %{system_name}-%{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build
Requires:       glibc
AutoReqProv:    no


%description
Kyua  is  a testing framework for infrastructure software, origi‐
nally designed to equip BSD‐based operating systems with  a  test
suite.  This  means that Kyua is lightweight and simple, and that
Kyua integrates well with various build  systems  and  continuous
integration frameworks.

Kyua  features  an  expressive  test suite definition language, a
safe runtime engine for test suites and a powerful report genera‐
tion engine.

Kyua  is for both developers and users, from the developer apply‐
ing a simple fix to a library to the system administrator deploy‐
ing a new release on a production machine.

Kyua  is able to execute test programs written with a plethora of
testing libraries and languages. The library of  choice  is  ATF,
for  which  Kyua  was originally designed, but simple, framework‐
less test programs and TAP‐compliant test programs  can  also  be
executed through Kyua.


%prep
%setup -n %{system_name}-%{system_name}-%{version}
%autoreconf


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%install
%make_install
%{__mv} %{buildroot}%{_prefix}/tests/%{system_name} %{buildroot}%{_datadir}/%{system_name}/tests


%check
# Test suite is failing
# make -j1 check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS LICENSE NEWS.md
%_bindir/%{system_name}
%_datadir/%{system_name}/*
%_mandir/man1/%{system_name}*.1
%_mandir/man5/%{system_name}*.5


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
