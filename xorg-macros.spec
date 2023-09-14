%global debug_package %{nil}
%define _build_id_links none
%define system_name xorg-macros

Name:           EDO%{system_name}
Version:        1.20
Release:        1%{?dist}
Summary:        Macros used by the configure.ac scripts for Xorg modular packages.
License:        GPL
Vendor:         %{_vendor}
URL:            https://gitlab.freedesktop.org/xorg/util/macros
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}
BuildArch:      noarch


%description


%prep
%setup -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%check


%install
%make_install
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}
%{__mv} %{buildroot}%{_datadir}/util-macros/INSTALL %{buildroot}%{_docdir}/%{name}/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc INSTALL
%_datadir/aclocal/%{system_name}.m4
%_datadir/pkgconfig/%{system_name}.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
