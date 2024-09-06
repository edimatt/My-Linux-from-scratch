%global debug_package %{nil}
%define _build_id_links none
%define system_name bat

Name:           EDO%{system_name}
Version:        0.24.0
Release:        1%{?dist}
Summary:        A cat(1) clone with wings.
License:        Apache-2.0
URL:            https://github.com/sharkdp/bat
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel EDOgcc EDOzlib-devel
Requires:       glibc EDOgcc EDOzlib
AutoReqProv:    no


%description
A cat(1) clone with syntax highlighting and Git integration.


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
