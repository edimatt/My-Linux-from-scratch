%global debug_package %{nil}
%define _build_id_links none
%define system_name aspell-de

Name:           EDO%{system_name}
Version:        20161207
Release:        1%{?dist}
Summary:        German language support for aspell.
License:        GPL
URL:            http://aspell.net
Source0:        https://ftp.gnu.org/gnu/aspell/dict/de/%{system_name}-%{version}.tar.xz
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
