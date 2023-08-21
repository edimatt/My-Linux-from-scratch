%global debug_package %{nil}
%define _build_id_links none

Name:           multimarkdown
Version:        6.7.0
Release:        1%{?dist}
Summary:        Markdown processor.

License:        GPL
URL:            https://github.com/Efreak/ncdu
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rpm-build perl-Benchmark
Requires:       ncurses-libs glibc
AutoReqProv:    no

%description


%prep
%autosetup -n %{name}-%{version}


%build
%set_build_flags_with_rpath
%make_build
cd build && %make_build


%install
mkdir -p %{buildroot}%{_bindir}
cp build/multimarkdown %{buildroot}%{_bindir}/


%check
cd build && ctest


%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%{name}


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
