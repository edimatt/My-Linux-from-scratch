%global debug_package %{nil}
%define _build_id_links none
%define system_name tmux

Name:           EDO%{system_name}
Version:        3.4
Release:        1%{?dist}
Summary:        Terminal multiplexer.
License:        GPL
URL:            https://github.com/tmux/tmux
Source0:        https://github.com/tmux/tmux/releases/download/%{version}/%{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel EDOncurses-devel EDOlibevent-devel EDOlibutempter-devel EDOutf8proc-devel
Requires:       glibc EDOncurses-libs EDOlibevent EDOlibutempter EDOutf8proc
AutoReqProv:    no


%description
tmux  is a terminal multiplexer: it enables a number of terminals
to be created, accessed, and controlled  from  a  single  screen.
tmux  may  be  detached from a screen and continue running in the
background, then later reattached.
This release runs on OpenBSD, FreeBSD, NetBSD, Linux,  macOS  and
Solaris. See the changes for this release at: 
https://raw.githubusercontent.com/tmux/tmux/%{version}/CHANGES


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --enable-utempter -enable-utf8proc
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
