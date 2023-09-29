%global debug_package %{nil}
%define _build_id_links none
%define system_name meson

Name:           EDOpython-%{system_name}
Version:        1.2.1
Release:        1%{?dist}
Summary:        A high performance build system.
License:        Apache 2.0
URL:            https://mesonbuild.com
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no
BuildArch:      noarch

%description
Meson  is  an open source build system meant to be both extremely
fast, and, even more importantly, as user friendly as possible.
The main design point of Meson is that every moment  a  developer
spends writing or debugging build definitions is a second wasted.
So is every second spent waiting for the build system to actually
start compiling code.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath


%install
%pip_install
%{__rm} %{buildroot}%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%{_libdir}/python3.11/site-packages/%{system_name}*
%{_mandir}/man1/%{system_name}.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
