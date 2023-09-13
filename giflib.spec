%global debug_package %{nil}
%define _build_id_links none
%define system_name giflib

Name:           EDO%{system_name}
Version:        5.2.1
Release:        1%{?dist}
Summary:        A library and utilities for processing GIFs.
License:        GPL
Vendor:         %{_vendor}
URL:            https://giflib.sourceforge.net
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  EDOgcc glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The  GIFLIB  project  maintains the giflib service library, which
has been pulling images out of GIFs since 1989.  It  is  deployed
everywhere  you can think of and some places you probably can’t ‐
graphics applications and web browsers on multiple operating sys‐
tems, game consoles, smartphones, and likely your ATM too.

Yes,  this  code  is he reason GIFs were in Mosaic, the first web
browser that could do inline graphics; it is  the  implementation
Andreesen and Bina used.

This  is  very  mature, stable, small‐footprint code with minimal
dependencies (suitable for  use  in  embedded  deployments)  that
needs  only occasional very minor bugfixes. Test reports from odd
platforms and better regression tests are  particularly  welcome.
Don’t  try  to  redesign  it,  applications beyond counting would
break if you did.

It’s "GIFLIB" in caps as a nod to the code’s origins in the  dark
and  backward abysm of MS‐DOS, but Unix hackers are encouraged to
spell it "giflib" in deference to local conventions. :‐)

Before October 2006 the GIF format was encumbered by  patents  on
the  LZW  compression it uses. This first became an issue in 1993
when the patent‐holders made  ambiguous  noises  about  requiring
royalties.  For some time a subset of this code travelled as "li‐
bungif", supporting decompression but not  compression.  You  can
read a more detailed history here.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%make_build CFLAGS="$CFLAGS -fPIC" OFLAGS=


%check


%install
%make_install PREFIX=%_prefix LIBDIR=%_libdir


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/gif*
%_mandir/man1/gif*.1
%_libdir/libgif.so.7*
%_libdir/libgif.a


%files devel
%_includedir/gif_lib.h
%_libdir/libgif.so


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
