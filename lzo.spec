%global debug_package %{nil}
%define __brp_strip_lto %{nil}
%define _build_id_links none
%define system_name lzo

Name:           EDO%{system_name}
Version:        2.10
Release:        1%{?dist}
Summary:        Real time data compression library.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.oberhumer.com/opensource/lzo
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
LZO  is  a  portable lossless data compression library written in
ANSI C.  Offers pretty fast compression and *extremely* fast  de‐
compression.   One  of  the fastest compression and decompression
algorithms around. See the ratings for lzop in the famous Archive
Comparison Test .  Includes slower compression levels achieving a
quite competitive compression ratio while still decompressing  at
this  very  high  speed.   Distributed under the terms of the GNU
General Public License (GPL v2+). Commercial licenses are  avail‐
able through our LZO Professional license program.


%description devel
The lzo-devel package contains the header files and libraries needed
to develop programs that use the lzo compression library.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --enable-shared --docdir=%_docdir/%{name}
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc AUTHORS COPYING NEWS THANKS LZO.FAQ LZO.TXT LZOAPI.TXT
%_libdir/lib%{system_name}2.so.2*


%files devel
%_includedir/%{system_name}/*.h
%_libdir/lib%{system_name}2.so
%_libdir/lib%{system_name}2.la
%_libdir/pkgconfig/lzo2.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
