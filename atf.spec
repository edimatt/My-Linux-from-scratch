%global debug_package %{nil}
%define _build_id_links none
%define system_name atf

Name:           EDO%{system_name}
Version:        0.22
Release:        1%{?dist}
Summary:        ATF - Automated testing framework.
License:        GPL
URL:            https://github.com/jmmv/atf
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build EDOgcc EDOlibiconv-devel
Requires:       glibc EDOatf EDOgcc EDOlibiconv
AutoReqProv:    no


%description
ATF, or Automated Testing Framework, is a collection of libraries
to write test programs in C, C++ and POSIX shell.

The ATF libraries offer a  simple  API.  The  API  is  orthogonal
through  the  various  bindings,  allowing  developers to quickly
learn how to write test programs in different languages.

ATF‐based test programs offer a consistent end‐user  command‐line
interface to allow both humans and automation to run the tests.

ATF‐based test programs rely on an execution engine to be run and
this execution engine is not shipped with ATF. Kyua is the engine
of choice.


%prep
%setup -n %{system_name}-%{version}
autoreconf -fi


%build
%set_build_flags_with_rpath
%configure
%make_build


%install
%make_install
# Relocate tests inside the data dir.
mv %{buildroot}%{_prefix}/tests/%{system_name} %{buildroot}%{_datadir}/%{system_name}/tests


%check
make check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}-sh
%_libdir/lib%{system_name}*
%_libdir/pkgconfig/%{system_name}-*
%_libexecdir/%{system_name}-check
%_datadir/aclocal/%{system_name}-*.m4
%_datadir/%{system_name}/*
%_docdir/%{system_name}/*
%_mandir/man*/%{system_name}*.*
%_includedir/%{system_name}-c*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
