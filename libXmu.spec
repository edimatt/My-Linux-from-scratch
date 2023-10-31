%global debug_package %{nil}
%define _build_id_links none
%define system_name libXmu

Name:           EDO%{system_name}
Version:        1.1.4
Release:        1%{?dist}
Summary:        X miscellaneous utility routines library.
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/lib/libxmu
Source0:        https://gitlab.freedesktop.org/xorg/lib/libxmu/-/tags/%{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros EDOlibX11-devel EDOlibXext-devel EDOxproto EDOxextproto EDOlibXt-devel EDOlibxcb-devel EDOlibXau-devel EDOlibICE-devel EDOutil-linux EDOlibSM-devel
Requires:       glibc EDOlibX11 EDOlibXt EDOlibXext EDOlibxcb EDOlibXau EDOlibICE EDOutil-linux EDOlibSM
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
This  library contains miscellaneous utilities and is not part of
the Xlib standard.  It contains routines which  only  use  public
interfaces  so  that  it may be layered on top of any proprietary
implementation of Xlib or Xt.  It is intended to support  clients
in  the  X.Org distribution; vendors may choose not to distribute
this library if they wish.   Therefore,  applications  developers
who depend on this library should be prepared to treat it as part
of their software base when porting.  API documentation for  this
library  is provided in the docs directory in DocBook format.  If
xmlto is installed, it will be converted to supported formats and
installed in $(docdir) unless ‐‐disable‐docs is passed to config‐
ure.


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
%doc Xmu.xml xlogo.svg
%_libdir/%{system_name}*.so.*


%files devel
%_includedir/X11/Xmu/*
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/xmu*.pc

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
