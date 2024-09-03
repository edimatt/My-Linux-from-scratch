%global debug_package %{nil}
%define _build_id_links none
%define system_name kubernetes

Name:           EDO%{system_name}
Version:        1.31.0
Release:        1%{?dist}
Summary:        Production-Grade Container Scheduling and Management
License:        Apache 2.0
URL:            https://github.com/kubernetes/kubernetes
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  EDOmake
# Binaries are statically linked. No dependencies.
# Requires:       glibc
AutoReqProv:    no


%description
Kubernetes,  also known as K8s, is an open source system for man‐
aging containerized applications across multiple hosts.  It  pro‐
vides basic mechanisms for the deployment, maintenance, and scal‐
ing of applications.

Kubernetes builds upon a decade  and  a  half  of  experience  at
Google  running  production  workloads  at  scale  using a system
called Borg, combined with best‐of‐breed ideas and practices from
the community.

Kubernetes  is  hosted  by  the Cloud Native Computing Foundation
(CNCF). If your company wants to  help  shape  the  evolution  of
technologies  that are container‐packaged, dynamically scheduled,
and microservices‐oriented, consider joining the  CNCF.  For  de‐
tails  about who’s involved and how Kubernetes plays a role, read
the CNCF announcement.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
export GOPATH=%{_builddir}
export GOBIN=%{buildroot}%{_bindir}
%make_build all


%install
%__mkdir_p %{buildroot}%{_bindir}
install ./_output/bin/* %{buildroot}%{_bindir}


%clean
export GOPATH=%{_builddir}
go clean -modcache
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
