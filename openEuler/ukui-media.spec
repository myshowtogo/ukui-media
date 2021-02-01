%define debug_package %{nil}
Name:           ukui-media
Version:        3.0.2
Release:        3
Summary:        UKUI media utilities
License:        GPL-2+ GPL-3+ LGPL-2+ BSD-3-Clause
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

Autoreq : yes

BuildRequires: intltool
BuildRequires: qt5-qtbase-devel
BuildRequires: libcanberra-devel
BuildRequires: gsettings-qt-devel
BuildRequires: glib2-devel
BuildRequires: gsettings-qt-devel
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: mate-desktop-devel >= 1.18
BuildRequires: libmatemixer-devel >= 1.18
BuildRequires: libxml2-devel
BuildRequires: mate-common >= 1.18
BuildRequires: qt5-qtsvg-devel
BuildRequires: libqtxdg-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtmultimedia
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: qt5-qttools-devel

Requires: mate-desktop-libs >= 1.18
Requires: ukui-media-common = %{version}

Recommends: alsa-utils sound-theme-freedesktop

%description
 A simple and lightweight screensaver written by Qt5.
 The screensaver supports biometric auhentication which is
 provided by biometric-auth service.

%package common
Summary:	UKUI media utilities (common files)
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description common
 UKUI media utilities are the audio mixer and the volume
 control applet.
 .
 This package contains the common files.

%prep
%setup -q

%build
./autogen.sh --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib64
make

cd %{_builddir}/%{name}-%{version}/ukui-volume-control-applet-qt
mkdir build && cd build
qmake-qt5 ..
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
set -e
glib-compile-schemas /usr/share/glib-2.0/schemas/


%files
%{_sysconfdir}/xdg/autostart/ukui-volume-control-applet.desktop
%{_bindir}/ukui-volume-control
%{_bindir}/ukui-volume-control-applet
%{_datadir}/applications/ukui-volume-control.desktop
%{_datadir}/glib-2.0/schemas/org.ukui.media.gschema.xml
%{_datadir}/locale/af/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/am/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ar/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/as/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ast/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/az/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/be/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/bg/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/bn/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/bn_IN/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/br/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/bs/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ca/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/cmn/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/cs/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/cy/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/da/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/de/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/dz/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/el/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/en_AU/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/en_CA/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/es/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/es_AR/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/es_CO/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/es_MX/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/es_PR/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/et/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/eu/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/fa/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/fi/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/fr/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/fr_CA/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/frp/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ga/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/gl/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/gu/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/he/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/hi/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/hr/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/hu/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/hy/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/id/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/is/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/it/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ja/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/jv/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ka/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/kk/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/kn/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ko/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ku/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ku_IQ/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ky/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/lt/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/lv/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/mai/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/mg/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/mk/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ml/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/mn/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/mr/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ms/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/nb/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/nds/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ne/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/nl/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/nn/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/oc/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/or/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/pa/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/pl/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/pms/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/pt/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ro/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ru/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/rw/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/sc/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/si/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/sk/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/sl/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/sq/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/sr/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/sr@latin/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/sv/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ta/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/te/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/th/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/tk/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/tr/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ug/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/uk/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/ur/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/uz/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/vi/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/wa/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/xh/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/zh_HK/LC_MESSAGES/ukui-media.mo
%{_datadir}/locale/zh_TW/LC_MESSAGES/ukui-media.mo
%{_datadir}/man/man1/ukui-volume-control-applet-qt.1.gz
%{_datadir}/man/man1/ukui-volume-control-applet.1.gz
%{_datadir}/man/man1/ukui-volume-control.1.gz
%{_datadir}/sounds/ukui/default/alerts/bark.ogg
%{_datadir}/sounds/ukui/default/alerts/drip.ogg
%{_datadir}/sounds/ukui/default/alerts/glass.ogg
%{_datadir}/sounds/ukui/default/alerts/sonar.ogg
%{_datadir}/ukui-media/icons/hicolor/16x16/status/audio-input-microphone-high.png
%{_datadir}/ukui-media/icons/hicolor/16x16/status/audio-input-microphone-low.png
%{_datadir}/ukui-media/icons/hicolor/16x16/status/audio-input-microphone-medium.png
%{_datadir}/ukui-media/icons/hicolor/16x16/status/audio-input-microphone-muted.png
%{_datadir}/ukui-media/icons/hicolor/22x22/status/audio-input-microphone-high.png
%{_datadir}/ukui-media/icons/hicolor/22x22/status/audio-input-microphone-low.png
%{_datadir}/ukui-media/icons/hicolor/22x22/status/audio-input-microphone-medium.png
%{_datadir}/ukui-media/icons/hicolor/22x22/status/audio-input-microphone-muted.png
%{_datadir}/ukui-media/icons/hicolor/24x24/status/audio-input-microphone-high.png
%{_datadir}/ukui-media/icons/hicolor/24x24/status/audio-input-microphone-low.png
%{_datadir}/ukui-media/icons/hicolor/24x24/status/audio-input-microphone-medium.png
%{_datadir}/ukui-media/icons/hicolor/24x24/status/audio-input-microphone-muted.png
%{_datadir}/ukui-media/icons/hicolor/32x32/status/audio-input-microphone-high.png
%{_datadir}/ukui-media/icons/hicolor/32x32/status/audio-input-microphone-low.png
%{_datadir}/ukui-media/icons/hicolor/32x32/status/audio-input-microphone-medium.png
%{_datadir}/ukui-media/icons/hicolor/32x32/status/audio-input-microphone-muted.png
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-center-back-testing.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-center-back.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-center-testing.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-center.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-left-back-testing.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-left-back.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-left-side-testing.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-left-side.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-left-testing.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-left.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-right-back-testing.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-right-back.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-right-side-testing.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-right-side.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-right-testing.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-speaker-right.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-subwoofer-testing.svg
%{_datadir}/ukui-media/icons/hicolor/48x48/devices/audio-subwoofer.svg
%{_datadir}/ukui-media/icons/hicolor/scalable/status/audio-input-microphone-high.svg
%{_datadir}/ukui-media/icons/hicolor/scalable/status/audio-input-microphone-low.svg
%{_datadir}/ukui-media/icons/hicolor/scalable/status/audio-input-microphone-medium.svg
%{_datadir}/ukui-media/icons/hicolor/scalable/status/audio-input-microphone-muted.svg
%{_datadir}/ukui-media/sounds/ukui-sounds-default.xml

%changelog
* Mon Feb 1 2021 lvhan <lvhan@kylinos.cn> - 3.0.2-3
- update to upstream version 3.0.1-1

* Mon Dec 7 2020 lvhan <lvhan@kylinos.cn> - 3.0.2-2
- fix vol icon bug

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.2-1
- update to upstream version 3.0.1-1+1026

* Mon Sep 14 2020 douyan <douyan@kylinos.cn> - 2.0.4-1
- update to upstream version 2.0.4-2+0806

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 2.0.3-1
- Init package for openEuler
