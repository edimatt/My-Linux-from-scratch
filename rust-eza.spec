%global debug_package %{nil}
%define _build_id_links none
%define system_name eza

Name:           EDO%{system_name}
Version:        0.19.2
Release:        1%{?dist}
Summary:        A modern alternative to ls
License:        MIT
URL:            https://github.com/eza-community/eza
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel EDOgcc EDOzlib-devel
Requires:       glibc EDOgcc EDOzlib
AutoReqProv:    no


%description
eza  is  a modern, maintained replacement for the venerable file‐
listing command‐line program ls that ships with  Unix  and  Linux
operating  systems,  giving it more features and better defaults.
It uses colours to distinguish file types and metadata. It  knows
about  symlinks,  extended  attributes,  and Git. And itâs small,
fast, and just one single binary.
By deliberately making some decisions differently,  eza  attempts
to be a more featureful, more user‐friendly version of ls.


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
