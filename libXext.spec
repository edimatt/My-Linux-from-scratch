%global debug_package %{nil}
%define _build_id_links none
%define system_name libXext

Name:           EDO%{system_name}
Version:        1.3.5
Release:        1%{?dist}
Summary:        Library for common extensions to the X11 protocol.
License:        GPL
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/lib/libxext
Source0:        https://gitlab.freedesktop.org/xorg/lib/libxext/-/tags/%{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros EDOncompress EDOlibX11-devel EDOlibxcb-devel EDOlibXau-devel EDOxproto EDOxextproto
Requires:       glibc EDOlibX11 EDOlibxcb EDOlibXau
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
libXext  is  the historical libX11‐based catchall library for the
X11 extensions without their own libraries.   No  new  extensions
should  be added to this library ‐ it is now instead preferred to
make per‐extension libraries that can be evolved as needed  with‐
out breaking compatibility of this core library.


%description devel


%prep
%setup -q -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name} --disable-stat-zfile
%make_build


%check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_docdir/%{name}/*
%_libdir/%{system_name}.so.*


%files devel
%_includedir/X11/*
%_mandir/man3/*.3
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/xext.pc

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
