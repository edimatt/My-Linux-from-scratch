%global debug_package %{nil}
%define _build_id_links none
%define system_name libpng

Name:           EDO%{system_name}
Version:        1.6.40
Release:        1%{?dist}
Summary:        The official PNG reference library.
License:        GPL
Vendor:         %{_vendor}
URL:            http://www.libpng.org/pub/png/libpng.html
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOzlib-devel
Requires:       glibc EDOzlib
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
libpng  is the official PNG reference library. It supports almost
all PNG features, is extensible, and has been extensively  tested
for  over 28 years. The home site for development versions (i.e.,
may be buggy or subject to change or  include  experimental  fea‐
tures) is https://libpng.sourceforge.io/, and the place to go for
questions about the  library  is  the  png‐mng‐implement  mailing
list.

libpng is available as ANSI C (C89) source code and requires zlib
1.0.4 or later (1.2.13 or later recommended for  performance  and
security  reasons). The current public release, libpng 1.6.40, is
a maintenance release with various fixes and improvements to  the
build  scripts,  docs,  and handlers for three of the chunk types
(eXIf, pCAL, tRNS).


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
%_bindir/png*
%_libdir/%{system_name}*.so.16*


%files devel
%_bindir/%{system_name}*-config
%_mandir/man3/%{system_name}*.3
%_mandir/man5/png.5
%_includedir/*png*.h
%_includedir/%{system_name}16/*.h
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
