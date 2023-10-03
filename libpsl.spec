%global debug_package %{nil}
%define _build_id_links none
%define system_name libpsl

Name:           EDO%{system_name}
Version:        0.21.2
Release:        1%{?dist}
Summary:        C library for the Public Suffix List
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/rockdaboot/libpsl
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOlibunistring-devel EDOlibidn2-devel EDOlibiconv-devel
Requires:       glibc EDOlibunistring EDOlibidn2 EDOlibiconv
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
A  Public Suffix List is a collection of Top Level Domains (TLDs)
suffixes. TLDs include Global Top Level Domains (gTLDs) like .com
and  .net;  Country  Top Level Domains (ccTLDs) like .de and .cn;
and Brand Top Level Domains like .apple and .google.  Brand  TLDs
allows users to register their own top level domain that exist at
the same level as ICANN’s gTLDs. Brand  TLDs  are  sometimes  re‐
ferred to as Vanity Domains.

Browsers, web clients and other user agents can use a public suf‐
fix list to:

avoid privacy‐leaking "supercookies";
avoid privacy‐leaking "super domain" certificates  (see post from
Jeffry Walton);
domain highlighting parts of the domain in a user interface;
sorting domain lists by site.

Libpsl...

has  built‐in  PSL  data for fast access (DAWG/DAFSA reduces size
from 180kB to ~32kB) allows to load PSL data from files checks if
a given domain is a "public suffix" provides immediate cookie do‐
main verification finds the longest public part of a given domain
finds  the shortest private part of a given domain works with in‐
ternational domains (UTF‐8 and IDNA2008 Punycode) is  thread‐safe
handles IDNA2008 UTS#46 (if libicu is available)


%description devel


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --with-python_prefix=%_prefix --docdir=%_docdir/%{name} 
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/psl
%_mandir/man1/psl*.1
%_libdir/%{system_name}.so.5*


%files devel
%_includedir/%{system_name}.h
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/%{system_name}.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
