%global debug_package %{nil}
%define _build_id_links none
%define system_name aspell-en

Name:           EDO%{system_name}
Version:        2020.12.07
Release:        1%{?dist}
Summary:        English language support for aspell.
License:        GPL
URL:            http://aspell.net
Source0:        https://ftp.gnu.org/gnu/aspell/dict/en/%{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build EDOaspell
Requires:       bash EDOaspell
BuildArch:      noarch
AutoReqProv:    no

%description


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
./configure
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/aspell*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
