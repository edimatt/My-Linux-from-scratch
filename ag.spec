%global debug_package %{nil}
%define _build_id_links none

Name:           ag
Version:        2.2.0
Release:        1%{?dist}
Summary:        A code searching tool similar to ack, with a focus on speed.

License:        GPL
URL:            https://github.com/htop-dev/htop
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rpm-build glibc-devel pcre-devel xz-devel zlib-devel
Requires:       glibc pcre xz-libs zlib
AutoReqProv:    no


%description

%prep
%autosetup -n %{name}-%{version}
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
%_bindir/%{name}
%_mandir/man1/%{name}.1
%_datadir/the_silver_searcher/*
%_datadir/zsh/site-functions/_the_silver_searcher


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
