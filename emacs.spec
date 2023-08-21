%global debug_package %{nil}
%define _build_id_links none

Name:           emacs
Version:        29.1
Release:        1%{?dist}
Summary:        GNU Emacs text editor.

License:        GPL
URL:            https://github.com/emacs-mirror/emacs
Source0:        %{name}-%{name}-%{version}.tar.gz

BuildRequires:  nettle-devel zlib-devel giflib-devel libjpeg-turbo-devel gtk3-devel gnutls-devel libXpm-devel libjpeg-turbo-devel texinfo rpm-build ncurses-devel
Requires:       atk at-spi2-atk at-spi2-core bzip2-libs cairo cairo-gobject dbus-libs fontconfig freetype fribidi gdk-pixbuf2 giflib glib2 glibc gmp gnutls graphite2 gtk3 harfbuzz jbigkit-libs json-glib libblkid libbrotli libcap libdatrie libepoxy libffi libgcc libgcrypt libgpg-error libicu libidn2 libjpeg-turbo libmount libpng libselinux libstdc++ libstemmer libtasn1 libthai libtiff libtracker-sparql libunistring libwayland-client libwayland-cursor libwayland-egl libwebp libX11 libX11-xcb libXau libxcb libXcomposite libXcursor libXdamage libXext libXfixes libXi libXinerama libxkbcommon libxml2 libXrandr libXrender libzstd lz4-libs ncurses-libs nettle p11-kit pango pcre pcre2 pixman sqlite-libs systemd-libs xz-libs zlib
AutoReqProv:    no

%description
GNU Emacs text editor.

%prep
%autosetup -n %{name}-%{name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%configure --disable-silent-rules --with-native-compilation --with-sound=yes --with-json=ifavailable
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/*
%_mandir/man1/*
/opt/edo/libexec/%name/*
%_includedir/%name-module.h
/opt/edo/lib64/systemd/user/%name.service
%_datadir/%name/*
%_datadir/metainfo/%name.metainfo.xml
%_datadir/applications/%{name}*
%_infodir/*
%_datadir/icons/*
%_libdir/%{name}/%{version}/native-lisp/*

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
