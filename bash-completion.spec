%global debug_package %{nil}
%define _build_id_links none
%define system_name bash-completion

Name:           EDO%{system_name}
Version:        2.11
Release:        1%{?dist}
Summary:        Programmable completion functions for bash.
License:        GPL
URL:            https://github.com/scop/bash-completion
Source:         %{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build glibc-devel
Requires:       glibc

AutoReqProv:    no

%description
bash‐completion  is  a collection of command line command comple‐
tions for the Bash shell, collection of helper functions  to  as‐
sist in creating new completions, and set of facilities for load‐
ing completions automatically on demand, as  well  as  installing
them.


%prep
%setup -n %{system_name}-%{version}
%autoreconf


%build
%set_build_flags_with_rpath
%_configure
%make_build


%install
%make_install
%{__mkdir_p} %{buildroot}%{_libdir}/pkgconfig
%{__mv} %{buildroot}%{_datadir}/pkgconfig/* %{buildroot}%{_libdir}/pkgconfig/


%check
# make check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc AUTHORS COPYING
%_datadir/%{system_name}/*
%_datadir/cmake/%{system_name}/*
%_libdir/pkgconfig/%{system_name}.pc
%_sysconfdir/profile.d/bash_completion.sh


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
