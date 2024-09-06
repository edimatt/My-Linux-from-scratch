%global debug_package %{nil}
%define _build_id_links none
%define system_name procs

Name:           EDO%{system_name}
Version:        0.14.6
Release:        1%{?dist}
Summary:        A modern replacement for ps written in Rust
License:        MIT
URL:            https://github.com/dalance/procs
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel EDOgcc
Requires:       glibc EDOgcc
AutoReqProv:    no


%description


%prep
%setup -q -n %{system_name}-%{version}


%build



%install
export DESTDIR=%{buildroot}
cargo install --locked --root %{buildroot}%_prefix --path .


%files
%_bindir/%{system_name}
%exclude %_prefix/.crates.toml
%exclude %_prefix/.crates2.json


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
