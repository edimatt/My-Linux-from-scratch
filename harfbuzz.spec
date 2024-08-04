%global debug_package %{nil}
%define _build_id_links none
%define system_name harfbuzz

Name:           EDO%{system_name}
Version:        2.9.1
Release:        1%{?dist}
Summary:        Text shaping library
License:        MIT
URL:            https://harfbuzz.github.io/
Source0:        %{system_name}-%{version}.tar.gz
BuildRequires:  glibc-devel EDOgcc
Requires:       glibc EDOgcc
Provides:       %{name} = %{version}
AutoReqProv:    no


%package devel
Summary:        Devel libraries and headers for %{system_name}.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
HarfBuzz  is  a  text shaping library. Using the HarfBuzz library
allows programs to convert a sequence of Unicode input into prop‐
erly formatted and positioned glyph outputâfor any writing system
and language.

The canonical source‐code tree is available  at  github.com/harf‐
buzz/harfbuzz. See Downloading HarfBuzz for release tarballs.


%description devel
Devel libraries and headers for %{system_name}.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%cmake_setup
%cmake_build


%install
%cmake_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/lib%{system_name}*.so


%files devel
%_libdir/cmake/%{system_name}/*.cmake
# %_libdir/pkgconfig/%{system_name}*.pc
%_includedir/%{system_name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- Warning: Starting from version 3.0, the header hb-ft.h is missing.
- This breaks freetype, and consequently, cairo.
