%global debug_package %{nil}
%define _build_id_links none
%undefine __brp_mangle_shebangs
%define system_name utf8proc

Name:           EDO%{system_name}
Version:        2.8.0
Release:        1%{?dist}
Summary:        Unicode library.
License:        GPL
URL:            https://juliastrings.github.io/utf8proc
Source0:        %{system_name}-%{version}.tar.gz
Patch:          %{system_name}-%{version}-setpaths.patch
Provides:       %{name}-%{version}
BuildRequires:  glibc-devel
Requires:       glibc
AutoReqProv:    no


%package devel
Summary:        Development tools.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
utf8proc  is  a small, clean C library that provides Unicode nor‐
malization, case‐folding, and other operations for  data  in  the
UTF‐8 encoding. It was initially developed by Jan Behrens and the
rest of the Public Software Group, who deserve nearly all of  the
credit for this package. With the blessing of the Public Software
Group, the  Julia  developers  have  taken  over  development  of
utf8proc,  since  the  original  developers  have  moved to other
projects.

(utf8proc is used for basic Unicode support  in  the  Julia  lan‐
guage,  and  the  Julia  developers  became involved because they
wanted to add Unicode 7 support and other features.)

(The original utf8proc package also includes Ruby and  PostgreSQL
plug‐ins. We removed those from utf8proc in order to focus exclu‐
sively on the C library for the time being, but plan to add  them
back in or release them as separate packages.)

The  utf8proc  package is licensed under the free/open‐source MIT
"expat" license (plus certain Unicode data governed by the  simi‐
larly  permissive  Unicode data license); please see the included
LICENSE.md file for more detailed information.


%description devel


%prep
%setup -n %{system_name}-%{version}
%patch -p0



%build
%make_build


%install
%make_install prefix=%_prefix


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/lib%{system_name}.so.2.6.0
%_libdir/lib%{system_name}.so.2
%_libdir/lib%{system_name}.a


%files devel
%_libdir/lib%{system_name}.so
%_includedir/%{system_name}.h
%_libdir/pkgconfig/lib%{system_name}.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
