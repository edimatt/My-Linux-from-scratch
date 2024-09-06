%global debug_package %{nil}
%define _build_id_links none
%define system_name ripgrep

Name:           EDO%{system_name}
Version:        14.1.0
Release:        1%{?dist}
Summary:        Search directories recursively for a regex pattern while respecting your gitignore
License:        MIT
URL:            https://github.com/eza-community/eza
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel EDOgcc
Requires:       glibc EDOgcc
AutoReqProv:    no


%description
ripgrep  is a line‐oriented search tool that recursively searches
the current directory for a regex pattern.  By  default,  ripgrep
will  respect  gitignore  rules  and  automatically  skip  hidden
files/directories and binary files.  (To  disable  all  automatic
filtering  by default, use rg ‐uuu.) ripgrep has first class sup‐
port on Windows, macOS and Linux, with binary downloads available
for  every  release.  ripgrep  is similar to other popular search
tools like The Silver Searcher, ack and grep.


%prep
%setup -q -n %{system_name}-%{version}


%build


%install
export DESTDIR=%{buildroot}
cargo install --locked --root %{buildroot}%_prefix --path .


%files
%_bindir/rg
%exclude %_prefix/.crates.toml
%exclude %_prefix/.crates2.json


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
