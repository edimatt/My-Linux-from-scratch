%global debug_package %{nil}
%define _build_id_links none
%define system_name libXau

Name:           EDO%{system_name}
Version:        1.0.11
Release:        1%{?dist}
Summary:        A Sample Authorization Protocol for X.
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/lib/libxau
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc
Requires:       glibc EDOgcc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
This  is  a very simple mechanism for providing individual access
to an X Window System display.It uses existing core protocol  and
library hooks for specifying authorization data in the connection
setup block to restrict use of the display to only those  clients
that  show  that  they know a server‐specific key called a "magic
cookie".


%description devel


%prep
%setup -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
# export CFLAGS="-O3 -g -Wall"
# export CXXFLAGS="$CFLAGS"
%_configure --enable-only64bit --enable-lto --enable-tls
%make_build


%check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/%{system_name}.so.6*


%files devel
%_includedir/X11/Xauth.h
%_libdir/%{system_name}.so
%_libdir/%{system_name}.la
%_libdir/pkgconfig/xau.pc
%_mandir/man3/Xau*.3


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
