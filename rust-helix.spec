%global debug_package %{nil}
%define _build_id_links none
%define system_name helix

Name:           EDO%{system_name}
Version:        24.07
Release:        1%{?dist}
Summary:        A post-modern modal text editor.
License:        MPL-2.0
URL:            https://helix-editor.com
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel EDOgcc
Requires:       glibc EDOgcc
AutoReqProv:    no


%description
A Kakoune / Neovim inspired editor, written in Rust.
The editing model is very heavily based on Kakoune; during devel‐
opment I found myself agreeing with most of Kakoune’s design  de‐
cisions.
For more information, see the website or documentation.
All  shortcuts/keymaps  can  be found in the documentation on the
website.


%prep
%setup -q -n %{system_name}-%{version}


%build
export HELIX_DEFAULT_RUNTIME=%_libdir/%{system_name}/runtime
cargo build --profile opt --locked


%install
%__mkdir_p %{buildroot}%_libdir/%{system_name} 
%__mkdir_p %{buildroot}%_bindir
cp -r runtime %{buildroot}%_libdir/%{system_name}/
cp target/opt/hx %{buildroot}%_bindir/hx


%files
%_bindir/hx
%_libdir/%{system_name}/runtime/*
%exclude %_prefix/.crates.toml
%exclude %_prefix/.crates2.json


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
