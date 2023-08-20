%global debug_package %{nil}
%define _build_id_links none

Name:           rlwrap
Version:        0.46.1
Release:        1%{?dist}
Summary:        The readline wrapper.

License:        GPL
URL:            https://github.com/hanslub42/rlwrap
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rpm-build ncurses-devel readline-devel
Requires:       readline ncurses-libs glibc
AutoReqProv:    no

%description
rlwrap is a ’readline wrapper’, a small utility that uses the GNU
Readline library to allow the editing of keyboard input  for  any
command.

I  couldn’t  find  anything  like it when I needed it, so I wrote
this one back in 1999. By now, there are (and, in hindsight, even
then  there were) a number of good readline wrappers around, like
rlfe, distributed as part of the GNU readline  library,  and  the
amazing socat.

You  should  consider using rlwrap especially when you need user‐
defined completion (by way of completion word lists) and  persis‐
tent  history,  or if you want to program ’special effects’ using
the filter mechanism.

As it is often used with older or even obsolete software,  rlwrap
strives  to  compile and run on a fairly wide range of not neces‐
sarily recent Unix‐like systems (FreeBSD, OSX,  HP‐UX,  AIX,  So‐
laris,  QNX,  cygwin,  linux  and probably quite a few more) This
would not have been without  Polarhome’s  now  retired  ’dinosaur
zoo’ of ageing Unix systems


%prep
%autosetup -n %{name}-%{version}
autoreconf -fi
%configure

%build
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%name
%_mandir/man*
%_datadir/%name/*

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
