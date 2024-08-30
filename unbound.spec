%global debug_package %{nil}
%define _build_id_links none
%define system_name unbound

Name:           EDO%{system_name}
Version:        1.21.0
Release:        1%{?dist}
Summary:        Unbound is a validating, recursive, caching DNS resolver.
License:        GPL
Vendor:         %{_vendor}
URL:            https://nlnetlabs.nl/projects/unbound
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgmp-devel EDOexpat-devel EDOopenssl-devel
Requires:       glibc EDOgmp EDOexpat EDOopenssl-libs
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Unbound  is  a validating, recursive, caching DNS resolver. It is
designed to be fast and lean  and  incorporates  modern  features
based on open standards.

To  help  increase  online privacy, Unbound supports DNS‐over‐TLS
and DNS‐over‐HTTPS which allows clients to encrypt their communi‐
cation.  In  addition,  it supports various modern standards that
limit the amount of data exchanged  with  authoritative  servers.
These  standards do not only improve privacy but also help making
the DNS more robust. The most important are Query Name  Minimisa‐
tion,  the  Aggressive  Use of DNSSEC‐Validated Cache and support
for authority zones, which can be used to load a copy of the root
zone.

Unbound  runs on all Linux and BSD distributions, as well as mac‐
OS, with packages available for most platforms. It is included in
the  base‐system  of  all  major BSD operating systems and in the
standard repositories of most Linux  distributions.  Installation
and  configuration  is designed to be easy. Setting up a resolver
for your machine or network can be done with only a few lines  of
configuration.

It is free, open source software under the BSD license. The guid‐
ing principles for our product development roadmap are first  and
foremost  the  security and privacy of the user. In addition, all
functionality must be backed by well established open  standards.
We  continually  improve  the functionality of Unbound for all of
our users. This means we do not make  custom  builds  or  provide
specific  features  to  paying customers only. Our priorities are
guided by the feedback of our  user  base,  in  particular  those
users with a support contract, as well as the wider Internet com‐
munity. Sponsored functionality will be given a  higher  priority
where possible and is evaluated on a case‐by‐case basis.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --disable-static --disable-sha1 --with-ssl=%_prefix --with-libexpat=%_prefix
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_sbindir/%{system_name}*
%_libdir/lib%{system_name}*.so.8*
%_mandir/man1/%{system_name}*
%_sysconfdir/%{system_name}/%{system_name}.conf


%files devel
%_includedir/%{system_name}.h
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}.la
%_libdir/pkgconfig/lib%{system_name}*.pc
%_mandir/man3/ub_*
%_mandir/man3/lib%{system_name}.3
%_mandir/man8/%{system_name}*
%_mandir/man5/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
