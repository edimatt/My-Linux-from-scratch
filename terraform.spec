%global debug_package %{nil}
%define _build_id_links none
%define system_name terraform

Name:           EDO%{system_name}
Version:        1.10.0
Release:        1%{?dist}
Summary:        Infrastructure as code.
License:        GPL
URL:            https://github.com/hashicorp/terraform
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel
Requires:       glibc
AutoReqProv:    no


%description
Terraform is a tool for building, changing, and versioning infra‐
structure safely and efficiently. Terraform can  manage  existing
and  popular  service  providers as well as custom in‐house solu‐
tions.

The key features of Terraform are:

Infrastructure as Code: Infrastructure is described using a high‐
level configuration syntax. This allows a blueprint of your data‐
center to be versioned and treated as you would any  other  code.
Additionally, infrastructure can be shared and re‐used.

Execution  Plans: Terraform has a "planning" step where it gener‐
ates an execution plan. The execution plan shows  what  Terraform
will  do  when  you call apply. This lets you avoid any surprises
when Terraform manipulates infrastructure.

Resource Graph: Terraform builds a graph of all  your  resources,
and  parallelizes the creation and modification of any non‐depen‐
dent resources. Because of this, Terraform builds  infrastructure
as efficiently as possible, and operators get insight into depen‐
dencies in their infrastructure.

Change  Automation: Complex changesets can be applied to your in‐
frastructure with minimal human interaction. With the  previously
mentioned  execution  plan  and  resource graph, you know exactly
what Terraform will change and in what order, avoiding many  pos‐
sible human errors.

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
