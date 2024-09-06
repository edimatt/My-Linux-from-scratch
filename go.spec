%global debug_package %{nil}
%define _build_id_links none
%define __os_install_post %{nil}
%define system_name go

Name:           EDO%{system_name}
Version:        1.23.0
Release:        1%{?dist}
Summary:        The go programming language
License:        GPL
URL:            https://go.dev
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  EDOmake
# Binaries are statically linked. No dependencies.
# Requires:       glibc
AutoReqProv:    no


%description
Build  simple,  secure,  scalable systems with Go. An open‐source
programming language supported by  Google.   Easy  to  learn  and
great  for  teams. Built‐in concurrency and a robust standard li‐
brary.  Large ecosystem of partners, communities, and tools


%prep
%setup -q -n %{system_name}-%{version}


%build
export GOROOT=%_libdir/go
export GOROOT_BOOTSTRAP=$(go env GOROOT)
export GOPATH=%{_builddir}
cd src
./make.bash


%install
%__mkdir_p %{buildroot}%{_bindir}
%__mkdir_p %{buildroot}%{_libdir}/%{system_name}
%__mkdir_p %{buildroot}%{_sysconfdir}/profile.d
cp -r api bin codereview.cfg go.env lib misc pkg src test %{buildroot}%{_libdir}/%{system_name}/
cd %{buildroot}%{_bindir} 
ln -s ../%{_lib}/%{system_name}/bin/%{system_name} .
ln -s ../%{_lib}/%{system_name}/bin/%{system_name}fmt .


%clean
export GOPATH=%{_builddir}
go clean -modcache
rm -rf $RPM_BUILD_ROOT


%files
%doc CONTRIBUTING.md README.md SECURITY.md PATENTS VERSION doc
%license LICENSE
%_bindir/*
%_libdir/%{system_name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
