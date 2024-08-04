%global debug_package %{nil}
%define _build_id_links none
%define system_name freetype

Name:           EDO%{system_name}
Version:        2.13.2
Release:        1%{?dist}
Summary:        Freely available software library to render fonts.
License:        GPL
Vendor:         %{_vendor}
URL:            https://freetype.org/
Source0:        https://download.savannah.gnu.org/releases/freetype/%{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOautoconf make EDOgcc EDObzip2-devel EDOlibpng-devel EDOzlib-devel EDObrotli-devel EDOharfbuzz-devel
Requires:       glibc EDOgcc EDObzip2-libs EDOlibpng EDOzlib EDObrotli-libs EDOharfbuzz
Provides:       %{name} = %{version}


%package devel
Summary:        Devel libraries and headers for %{system_name}.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
FreeType is a freely available software library to render fonts.

It  is written in C, designed to be small, efficient, highly cus‐
tomizable, and portable while capable of  producing  high‐quality
output (glyph images) of most vector and bitmap font formats.


%description devel


%prep
%setup -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%check
# Requires the kyua framework.
# make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/lib%{system_name}.so.*


%files devel
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}.la
%_libdir/pkgconfig/%{system_name}2.pc
%_includedir/%{system_name}2/*
%_datadir/aclocal/%{system_name}2.m4


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
