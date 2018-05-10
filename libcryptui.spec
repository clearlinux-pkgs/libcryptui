#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcryptui
Version  : 3.12.2
Release  : 7
URL      : https://download.gnome.org/sources/libcryptui/3.12/libcryptui-3.12.2.tar.xz
Source0  : https://download.gnome.org/sources/libcryptui/3.12/libcryptui-3.12.2.tar.xz
Summary  : UI library for DBUS functions exported by Seahorse
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0 LGPL-2.0
Requires: libcryptui-bin
Requires: libcryptui-lib
Requires: libcryptui-data
Requires: libcryptui-doc
Requires: libcryptui-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gnupg
BuildRequires : gnupg-bin
BuildRequires : gobject-introspection-dev
BuildRequires : gpgme-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gnome-keyring-1)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(sm)
Patch1: build.patch

%description
Libcryptui: Interface components for OpenPGP
libcryptui is a library used for prompting for PGP keys. It's likely that this
library will become deprecated in the near future.

%package bin
Summary: bin components for the libcryptui package.
Group: Binaries
Requires: libcryptui-data

%description bin
bin components for the libcryptui package.


%package data
Summary: data components for the libcryptui package.
Group: Data

%description data
data components for the libcryptui package.


%package dev
Summary: dev components for the libcryptui package.
Group: Development
Requires: libcryptui-lib
Requires: libcryptui-bin
Requires: libcryptui-data
Provides: libcryptui-devel

%description dev
dev components for the libcryptui package.


%package doc
Summary: doc components for the libcryptui package.
Group: Documentation

%description doc
doc components for the libcryptui package.


%package lib
Summary: lib components for the libcryptui package.
Group: Libraries
Requires: libcryptui-data

%description lib
lib components for the libcryptui package.


%package locales
Summary: locales components for the libcryptui package.
Group: Default

%description locales
locales components for the libcryptui package.


%prep
%setup -q -n libcryptui-3.12.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509392850
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1509392850
rm -rf %{buildroot}
%make_install
%find_lang cryptui

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/seahorse-daemon

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/CryptUI-0.0.typelib
/usr/share/GConf/gsettings/org.gnome.seahorse.recipients.convert
/usr/share/cryptui/ui/seahorse-notify.xml
/usr/share/cryptui/ui/seahorse-pgp-generate.xml
/usr/share/cryptui/ui/seahorse-progress.xml
/usr/share/dbus-1/services/org.gnome.seahorse.service
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.seahorse.recipients.gschema.xml
/usr/share/pixmaps/cryptui/22x22/seahorse-key-personal.png
/usr/share/pixmaps/cryptui/22x22/seahorse-key-ssh.png
/usr/share/pixmaps/cryptui/22x22/seahorse-key.png
/usr/share/pixmaps/cryptui/22x22/seahorse-person.png
/usr/share/pixmaps/cryptui/22x22/seahorse-sign-bad.png
/usr/share/pixmaps/cryptui/22x22/seahorse-sign-ok.png
/usr/share/pixmaps/cryptui/22x22/seahorse-sign.png
/usr/share/pixmaps/cryptui/48x48/seahorse-key-personal.png
/usr/share/pixmaps/cryptui/48x48/seahorse-key-ssh.png
/usr/share/pixmaps/cryptui/48x48/seahorse-key.png
/usr/share/pixmaps/cryptui/48x48/seahorse-person.png
/usr/share/pixmaps/cryptui/48x48/seahorse-sign-bad.png
/usr/share/pixmaps/cryptui/48x48/seahorse-sign-ok.png
/usr/share/pixmaps/cryptui/48x48/seahorse-sign-unknown.png
/usr/share/pixmaps/cryptui/48x48/seahorse-sign.png
/usr/share/pixmaps/cryptui/scalable/seahorse-key-personal.svg
/usr/share/pixmaps/cryptui/scalable/seahorse-key-ssh.svg
/usr/share/pixmaps/cryptui/scalable/seahorse-key.svg
/usr/share/pixmaps/cryptui/scalable/seahorse-person.svg
/usr/share/pixmaps/cryptui/scalable/seahorse-sign-bad.svg
/usr/share/pixmaps/cryptui/scalable/seahorse-sign-ok.svg
/usr/share/pixmaps/cryptui/scalable/seahorse-sign-unknown.svg
/usr/share/pixmaps/cryptui/scalable/seahorse-sign.svg

%files dev
%defattr(-,root,root,-)
/usr/include/libcryptui/cryptui-key-chooser.h
/usr/include/libcryptui/cryptui-key-combo.h
/usr/include/libcryptui/cryptui-key-list.h
/usr/include/libcryptui/cryptui-key-store.h
/usr/include/libcryptui/cryptui-keyset.h
/usr/include/libcryptui/cryptui.h
/usr/lib64/libcryptui.so
/usr/lib64/pkgconfig/cryptui-0.0.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
/usr/share/gtk-doc/html/libcryptui/ch01.html
/usr/share/gtk-doc/html/libcryptui/home.png
/usr/share/gtk-doc/html/libcryptui/index.html
/usr/share/gtk-doc/html/libcryptui/index.sgml
/usr/share/gtk-doc/html/libcryptui/left-insensitive.png
/usr/share/gtk-doc/html/libcryptui/left.png
/usr/share/gtk-doc/html/libcryptui/libcryptui-cryptui-defines.html
/usr/share/gtk-doc/html/libcryptui/libcryptui-cryptui-key-chooser.html
/usr/share/gtk-doc/html/libcryptui/libcryptui-cryptui-key-combo.html
/usr/share/gtk-doc/html/libcryptui/libcryptui-cryptui-key-list.html
/usr/share/gtk-doc/html/libcryptui/libcryptui-cryptui-key-store.html
/usr/share/gtk-doc/html/libcryptui/libcryptui-cryptui-keyset.html
/usr/share/gtk-doc/html/libcryptui/libcryptui-cryptui-marshal.html
/usr/share/gtk-doc/html/libcryptui/libcryptui-cryptui.html
/usr/share/gtk-doc/html/libcryptui/libcryptui.devhelp2
/usr/share/gtk-doc/html/libcryptui/right-insensitive.png
/usr/share/gtk-doc/html/libcryptui/right.png
/usr/share/gtk-doc/html/libcryptui/style.css
/usr/share/gtk-doc/html/libcryptui/up-insensitive.png
/usr/share/gtk-doc/html/libcryptui/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcryptui.so.0
/usr/lib64/libcryptui.so.0.0.0

%files locales -f cryptui.lang
%defattr(-,root,root,-)

