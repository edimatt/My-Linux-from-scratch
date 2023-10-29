%global debug_package %{nil}
%define _build_id_links none
%define system_name xcb-proto

Name:           EDO%{system_name}
Version:        1.15
Release:        1%{?dist}
Summary:        X Protocol Extensions.
License:        GPL
Vendor:         %{_vendor}
URL:            https://xcb.freedesktop.org
Source0:        https://xcb.freedesktop.org/dist/%{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOxorg-macros EDOpython
Requires:       glibc EDOpython
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
%__mv %{buildroot}%{_prefix}/lib/python%{python3_version} %{buildroot}%{_libdir}/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_datadir/xcb/*
%python3_sitearch/xcb*
%_libdir/pkgconfig/%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
