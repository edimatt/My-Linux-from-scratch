%global debug_package %{nil}
%define _build_id_links none
%define system_name ag

Name:           EDO%{system_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        A code searching tool similar to ack, with a focus on speed.

License:        GPL
URL:            https://github.com/ggreer/the_silver_searcher
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build glibc-devel pcre-devel EDOxz-devel EDOzlib-devel
Requires:       glibc pcre EDOxz-libs EDOzlib
AutoReqProv:    no


%description


%prep
%autosetup -n %{system_name}-%{version}
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
%license ag
%doc ag
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1
%_datadir/the_silver_searcher/*
%_datadir/zsh/site-functions/_the_silver_searcher


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
