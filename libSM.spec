%global debug_package %{nil}
%define _build_id_links none
%define system_name libSM

Name:           EDO%{system_name}
Version:        1.2.4
Release:        1%{?dist}
Summary:        X Session Management library.
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/lib/libsm
Source0:        https://gitlab.freedesktop.org/xorg/lib/libsm/-/tags/%{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros EDOxproto EDOutil-linux EDOxtrans EDOlibICE-devel
Requires:       glibc EDOlibICE EDOutil-linux
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description


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
%doc SMlib.xml xsmp.xml
%_libdir/%{system_name}.so.*


%files devel
%_includedir/X11/SM/*
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/sm.pc

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
