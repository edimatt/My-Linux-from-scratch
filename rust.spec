%global debug_package %{nil}
%define _build_id_links none
%define system_name rustc

Name:           EDO%{system_name}
Version:        1.80.1
Release:        1%{?dist}
Summary:        The rust programming language
License:        GPL
URL:            https://www.rust-lang.org/tools/install
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel EDOmake EDOgcc EDObrotli-devel EDOcurl-devel EDOkrb5-devel EDOlibiconv-devel EDOlibidn2-devel EDOlibpsl-devel EDOlibunistring-devel EDOnghttp2-devel EDOopenssl-devel EDOzlib-devel EDOzstd-devel
Requires:       glibc EDObrotli-libs EDOcurl EDOgcc EDOkrb5 EDOlibiconv EDOlibidn2 EDOlibpsl EDOlibunistring EDOnghttp2 EDOopenssl-libs EDOzlib EDOzstd
AutoReqProv:    no


%description
Rust  is a systems programming language that runs blazingly fast,
prevents segfaults, and guarantees thread safety.


%prep
%setup -q -n %{system_name}-%{version}
# Prepare config.toml file
cat <<EOF > config.toml
[build]
target = ["x86_64-unknown-linux-gnu"]
docs = false
vendor = true
extended = true
submodules = false
verbose = 1

[install]
prefix = "%{_prefix}"
sysconfdir = "/etc%{_prefix}"
libdir = "lib64"

[rust]
channel = "stable"

[dist]
src-tarball = false

[llvm]
targets = "X86"
link-shared = true
ninja = true
EOF


%build
%__python3 ./x.py build


%install
export DESTDIR=%{buildroot}
%__python3 ./x.py install
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_libdir}/rustlib/src/rust/library/core/src/unicode/printable.py
find %{buildroot} -type f -exec sed -i 's|%{buildroot}||g' {} +


%files
%{_bindir}/rust*
%{_bindir}/cargo*
%{_bindir}/clippy*
%{_libdir}/rustlib
%{_libdir}/libLLVM*
%{_libdir}/librustc*
%{_libdir}/libstd*.so
%{_prefix}/libexec/rust*
%{_mandir}/man1/rust*.1
%{_mandir}/man1/cargo*.1
%{_datadir}/doc/rust*
%{_datadir}/doc/cargo*
%{_datadir}/doc/clippy*
%{_datadir}/zsh/site-functions/_cargo
%{_sysconfdir}/bash_completion.d/cargo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
