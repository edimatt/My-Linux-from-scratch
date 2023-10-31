%global debug_package %{nil}
%define _build_id_links none
%define system_name libXaw

Name:           EDO%{system_name}
Version:        1.0.15
Release:        1%{?dist}
Summary:        X Athena Widget Set.
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/lib/libxaw
Source0:        https://gitlab.freedesktop.org/xorg/lib/libxaw/-/tags/%{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros EDOlibX11-devel EDOlibXext-devel EDOxproto EDOxextproto EDOlibXt-devel EDOlibxcb-devel EDOlibXau-devel EDOlibICE-devel EDOutil-linux EDOlibSM-devel EDOlibXpm-devel EDOlibXmu-devel
Requires:       glibc EDOlibX11 EDOlibXt EDOlibXext EDOlibxcb EDOlibXau EDOlibICE EDOutil-linux EDOlibSM EDOlibXpm EDOlibXmu
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Xaw is a widget set based on the X Toolkit Intrinsics (Xt) Library.


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
%_libdir/%{system_name}*.so.*
%_docdir/%{name}/*


%files devel
%_includedir/X11/Xaw/*
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/xaw*.pc
%_mandir/man3/Xaw.3

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
