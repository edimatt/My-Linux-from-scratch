%global debug_package %{nil}
%define _build_id_links none
%define system_name fontsproto

Name:           EDO%{system_name}
Version:        2.1.3
Release:        1%{?dist}
Summary:        X Fonts Extension
License:        MIT
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/proto/fontsproto
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  EDOgcc EDOxmlto EDOxorg-macros
Provides:       %{name} = %{version}
BuildArch:      noarch


%description


%prep
%setup -q -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_docdir/%{name}/*
%_includedir/X11/fonts/*.h
%_libdir/pkgconfig/%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
