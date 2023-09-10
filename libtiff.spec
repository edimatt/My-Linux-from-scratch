%global debug_package %{nil}
%define _build_id_links none
%define system_name libtiff

Name:           EDO%{system_name}
Version:        4.6.0
Release:        1%{?dist}
Summary:        LibTIFF - TIFF Library and Utilities.
License:        GPL
URL:            http://www.simplesystems.org/libtiff
Source0:        %{system_name}-v%{version}rc2.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build glibc-devel EDOxz-devel EDOzlib-devel EDOzstd-devel EDOgcc EDOlibjpeg-devel
Requires:       glibc EDOxz-libs EDOzlib EDOzstd EDOgcc EDOlibjpeg
AutoReqProv:    no


%package devel
Summary:        Development tools.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The LibTIFF software provides support for the Tag Image File Forâ
mat (TIFF), a widely used format for storing image data. The latâ
est  version of the TIFF specification is TIFF File Format Speciâ
fication. Included in this software distribution are:

‐ a library, libtiff, for reading and writing  TIFF  images  ‐  a
small  collection  of  tools  ‐ documentation for the library and
tools.

The  libtiff library, along with associated tool programs, should
handle  most  of  your needs for reading and writing TIFF images.
LibTIFF is portable software, supported on various operating sysâ
tems  including UNIX (Linux, BSD, MacOS X) and Windows.  Starting
with libtiff v4.6.0, the source code for most TIFF tools  (except
tiffinfo,  tiffdump, tiffcp and tiffset) was discontinued, due to
the lack of contributors able to address  reported  security  is‐
sues.  It will still be available in the source distribution, but
they will no longer be built by default, and  issues  related  to
them will no longer be accepted in the libtiff bug tracker.


%description devel
The libtiff-devel  package contains  libraries and header files
for developing applications that use libtiff.


%prep
%setup -n %{system_name}-v%{version}rc2
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure --with-docdir=%_docdir/%{name}
%make_build


%install
%make_install


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc ChangeLog LICENSE.md README.md RELEASE-DATE TODO VERSION
%_bindir/tiff*
%_libdir/%{system_name}*.so.6*


%files devel
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/%{system_name}*.pc
%_includedir/tiff*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
