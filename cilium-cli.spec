%global debug_package %{nil}
%define _build_id_links none
%define system_name cilium-cli

Name:           EDO%{system_name}
Version:        0.16.13
Release:        1%{?dist}
Summary:        CNI network for kubernetes.
License:        GPL
URL:            https://github.com/cilium/cilium-cli
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel
Requires:       glibc
AutoReqProv:    no


%description
Cilium  is  an  open source, cloud native solution for providing,
securing, and observing network connectivity  between  workloads,
fueled by the revolutionary Kernel technology eBPF.

Cilium is used to provide and transparently secure network
connectivity and load  balancing  between  application  workloads
such  as  application containers, processes, or VMs. Cilium oper‐
ates at Layer 3/4 to provide traditional networking and  security
services  as  well as Layer 7 to protect and secure use of modern
application protocols such as HTTP, gRPC, and Kafka. Cilium is  a
part  of  the Cloud Native Computing Foundation and is their most
advanced and widely used CNI for Kubernetes. Check out  the  Get‐
ting Started Guides to try it out.

Cilium  has  hundreds of adopters around the world including Bell
Canada, Capital One, Google, The New York Times,  and  Yahoo.  If
you are using Cilium, add yourself to the list today!


%prep
%setup -q -n %{system_name}-%{version}


%build
export GOPATH=%{_builddir}


%install
%set_build_flags_with_rpath
export BINDIR=%{_bindir}
%make_install



%clean
export GOPATH=%{_builddir}
go clean -modcache
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/cilium


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
