%global debug_package %{nil}
%define _build_id_links none
%define system_name multimarkdown

Name:           EDO%{system_name}
Version:        6.7.0
Release:        1%{?dist}
Summary:        Markdown processor.

License:        GPL
URL:            https://github.com/fletcher/MultiMarkdown-6
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build perl-Benchmark
Requires:       glibc
AutoReqProv:    no

%description


%prep
%autosetup -n %{system_name}-%{version}


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
%_bindir/%{system_name}


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
