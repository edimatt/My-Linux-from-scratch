%global debug_package %{nil}
%define _build_id_links none

Name:           iotop
Version:        1.23
Release:        1%{?dist}
Summary:        Top like utility for I/O

License:        GPL
URL:            https://github.com/Tomas-M/iotop
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rpm-build ncurses-devel
Requires:       glibc ncurses-libs
AutoReqProv:    no

%description
Is  your  Linux  server  too slow or load is too high? One of the
possible causes of such symptoms may be  high  IO  (input/output)
waiting  time,  which basically means that some of your processes
need to read or write to a hard drive while it is  too  slow  and
not ready yet, serving data for some other processes.

Common  practice  is  to use iostat ‐x in order to find out which
block device (hard drive) is slow, but this  information  is  not
always  helpful.  It  could  help you much more if you knew which
process reads or writes the most data from your slow disk, so you
could renice it using ionice or even kill it.

iotop  identifies  processes that use high amount of input/output
requests on your machine. It is similar to  the  well  known  top
utility,  but  instead of showing you what consumes CPU the most,
it lists processes by their IO usage. Inspired  by  iotop  Python
script  from  Guillaume  Chazarain,  rewritten in C by Vyacheslav
Trushkin and improved by Boian Bonev so it runs without Python at
all.

%prep
%setup -n %{name}-%{version}

%build
export O='$$O'
export ORIGIN='$ORIGIN'
export CFLAGS="${RPM_OPT_FLAGS} -I%_includedir"
export LDFLAGS="$LDFLAGS -L%_libdir -Wl,-rpath=%_libdir:\$ORIGIN/../lib64"
%make_build


%install
%__make install PREFIX=%{buildroot}%{_prefix} INSTALL='/usr/bin/install -p'


%clean
rm -rf $RPM_BUILD_ROOT

%files
%_sbindir/%{name}
%_mandir/man8/%{name}.8


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
