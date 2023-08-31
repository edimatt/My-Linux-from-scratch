%global debug_package %{nil}
%define _build_id_links none
%define system_name libunistring

Name:           EDO%{system_name}
Version:        1.1
Release:        1%{?dist}
Summary:        A library for manipulating Unicode strings.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.gnu.org/software/libunistring
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOlibiconv-devel
Requires:       glibc EDOlibiconv
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Text  files are nowadays usually encoded in Unicode, and may con‐
sist of very different scripts â from Latin  letters  to  Chinese
Hanzi  â, with many kinds of special characters â accents, right‐
to‐left writing marks, hyphens, Roman numbers, and much more. But
the  POSIX  platform  APIs for text do not contain adequate func‐
tions for dealing with  particular  properties  of  many  Unicode
characters. In fact, the POSIX APIs for text have several assump‐
tions at their base which don’t hold for Unicode text.

This library provides functions for manipulating Unicode  strings
and for manipulating C strings according to the Unicode standard.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --disable-static
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/%{system_name}.so.5*


%files devel
%_includedir/uni*
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_docdir/%{system_name}/*

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
