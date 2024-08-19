%global debug_package %{nil}
%define _build_id_links none
%define system_name jid

Name:           EDO%{system_name}
Version:        0.7.6
Release:        1%{?dist}
Summary:        Json Incremental Digger
License:        MIT
URL:            https://github.com/simeji/jid
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel
Requires:       glibc
AutoReqProv:    no


%description
It’s  a  very simple tool.  You can drill down JSON interactively
by using filtering queries like jq.
Suggestion and Auto completion of this tool will  provide  you  a
very comfortable JSON drill down.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath


%install
export GOPATH=%{_builddir}
export GOBIN=%{buildroot}%{_bindir}
go install ./cmd/jid


%clean
export GOPATH=%{_builddir}
go clean -modcache
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
