%global debug_package %{nil}
%define _build_id_links none
%define system_name tig

Name:           EDOtig
Version:        2.5.7
Release:        1%{?dist}
Summary:        Text mode interface to git.

License:        GPL
URL:            https://github.com/jonas/tig
Source0:        %{system_name}-%{system_name}-%{version}.tar.gz

BuildRequires:  rpm-build EDOncurses-devel
Provides:       %{name} = %{version}
Requires:       EDOncurses-libs
AutoReqProv:    no

%description
Tig is an ncurses‐based text‐mode interface for git. It functions
mainly as a Git repository browser, but can also assist in  stag‐
ing changes for commit at chunk level and act as a pager for out‐
put from various Git commands.


%prep
%autosetup -n %{system_name}-%{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%configure
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%{system_name}
%_sysconfdir/%{system_name}rc

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
