%global debug_package %{nil}
%define _build_id_links none
%define system_name zellij

Name:           EDO%{system_name}
Version:        0.40.1
Release:        1%{?dist}
Summary:        A terminal workspace with batteries included
License:        MIT
URL:            https://github.com/zellij-org/zellij
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel EDObrotli-devel EDOcurl-devel EDOgcc EDOkrb5-devel EDOlibiconv-devel EDOlibidn2-devel EDOlibpsl-devel EDOlibunistring-devel EDOnghttp2-devel EDOopenssl-devel EDOzlib-devel EDOzstd-devel 
Requires:       glibc EDObrotli-libs EDOcurl EDOgcc EDOkrb5 EDOlibiconv EDOlibidn2 EDOlibpsl EDOlibunistring EDOnghttp2 EDOopenssl-libs EDOzlib EDOzstd

AutoReqProv:    no


%description
Zellij  is  a  workspace aimed at developers, ops‐oriented people
and anyone who loves the terminal. Similar programs are sometimes
called "Terminal Multiplexers".
Zellij is designed around the philosophy that one must not sacri‐
fice simplicity for power, taking pride in its  great  experience
out  of the box as well as the advanced features it places at its
users’ fingertips.
Zellij is geared toward beginner and power users alike ‐ allowing
deep  customizability,  personal automation through layouts, true
multiplayer collaboration, unique UX features  such  as  floating
and  stacked  panes,  and  a plugin system allowing one to create
plugins in any language that compiles to WebAssembly.
You can get started by installing Zellij  and  checking  out  the
Screencasts & Tutorials.
For more details about our future plans, read about upcoming fea‐
tures in our roadmap.


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
