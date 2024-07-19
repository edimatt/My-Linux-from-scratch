%global debug_package %{nil}
%define _build_id_links none
%define system_name yq

Name:           EDO%{system_name}
Version:        4.44.2
Release:        1%{?dist}
Summary:        A lightweight and portable command-line YAML, JSON and XML processor
License:        GPL
URL:            https://github.com/mikefarah/yq
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel
Requires:       glibc
AutoReqProv:    no


%description
yq uses jq like syntax but works with yaml files as well as json,
xml, properties, csv and tsv. It doesn’t yet  support  everything
jq  does  ‐  but  it  does support the most common operations and
functions, and more is being added continuously.

yq is written in go ‐ so you can download a dependency free bina‐
ry  for your platform and you are good to go! If you prefer there
are a variety of package managers that can be  used  as  well  as
Docker and Podman, all listed below.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
export GOPATH=%{_builddir}
go build -o %{system_name}


%install
install -Dm 0755 %{system_name} %{buildroot}%{_bindir}/%{system_name}



%clean
export GOPATH=%{_builddir}
go clean -modcache
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
