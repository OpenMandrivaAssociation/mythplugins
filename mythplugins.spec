# Requires autofinder is confused, requires nonexistent packages (mythtv-mythweb)
%if %{_use_internal_dependency_generator}
%define __noautoreq 'pear(.*)'
%else
%define _requires_exceptions pear*
%endif

%define gitversion v0.25.2-16-gd5192
%define fixesdate 20120829
%define rel 1

%if %{fixesdate}
%define release %{fixesdate}.%{rel}
%else
%define release %{rel}
%endif

#####################
# Hardcode PLF build
%define build_plf 0
#####################

%if %{build_plf}
%define extrarelsuffix plf
%define distsuffix plf
%endif

Summary:	Official MythTV plugins
Name:		mythplugins
Version:	0.25.2
Release:	%{release}%{?extrarelsuffix}
URL:		http://www.mythtv.org/
License:	GPL
Group:		Video
Source0:	ftp://ftp.osuosl.org/pub/mythtv/%{name}-%{version}.tar.bz2
%if %{fixesdate}
Patch1:		fixes-%{gitversion}.patch
%endif
Patch100:	0100-lame-Allow-building-without-lame-libraries.patch

BuildRequires:	libmyth-devel >= %{version}
BuildRequires:	python-mythtv >= %{version}
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libvisual-0.4)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libcdaudio)
BuildRequires:	cdda-devel
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig(taglib)
BuildRequires:	python-curl
BuildRequires:	python-oauth
BuildRequires:	perl-XML-XPath
BuildRequires:	perl-Image-Size
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-DateTime-Format-ISO8601
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-XML-Simple
%if %{build_plf}
BuildRequires:	lame-devel
BuildRequires:	libfaad2-devel
%endif
# (cg) Remove these once they are required in the python-mythtv package
BuildRequires:	python-lxml
BuildRequires:	python-mysql
# (cg) Ditto for the perl-DateTime-Format-ISO pkg
BuildRequires:	perl(Class::Factory::Util)

%description
Mythplugins for MythTV.

%if %{build_plf}
This package is in restricted because it contains software that supports
codecs that may be covered by software patents.
%endif

%package -n mythtv-plugin-browser
Summary:	Full web browser for MythTV
URL: 		http://www.mythtv.org/
Group:		Video
Obsoletes:	mythbrowser < 0.20a-7
Requires:	mythtv-frontend >= %{version}

%description -n mythtv-plugin-browser
MythBrowser is a full web browser for MythTV.

%package -n mythtv-plugin-gallery
Summary: 	Gallery/slideshow module for MythTV
Group: 		Video
Requires:	mythtv-frontend >= %{version}
Obsoletes:	mythgallery < 0.20a-7

%description -n mythtv-plugin-gallery
A gallery/slideshow module for MythTV.

%package -n mythtv-plugin-game
Summary: 	Game frontend for MythTV
Group: 		Video
Requires:	mythtv-frontend >= %{version}
Obsoletes:	mythgame < 0.20a-7

%description -n mythtv-plugin-game
A game frontend for MythTV.

%package -n mythtv-plugin-music
Summary: 	The music player add-on module for MythTV
Group: 		Video
#Requires:	cdparanoia
Requires:	mythtv-frontend >= %{version}
Obsoletes:	mythmusic < 0.20a-7

%description -n mythtv-plugin-music
The music player add-on module for MythTV.

%if %{build_plf}
This package is in restricted because it contains software that supports
codecs that may be covered by software patents.
%endif

%package -n mythtv-plugin-netvision
Summary:  NetVision for MythTV
Group:    Video
Requires: mythtv-frontend >= %{version}

%description -n mythtv-plugin-netvision
NetVision for MythTV. View popular media website content.

%package -n mythtv-plugin-news
Summary: 	RSS News feed plugin for MythTV
Group: 		Video
Requires:	mythtv-frontend >= %{version}
Obsoletes:	mythnews < 0.20a-7

%description -n mythtv-plugin-news
An RSS News feed plugin for MythTV.

%package -n mythtv-plugin-weather
Summary: 	MythTV module that displays a weather forecast
Group: 		Video
Requires:	mythtv-frontend >= %{version}
Obsoletes:	mythweather < 0.20a-7

%description -n mythtv-plugin-weather
A MythTV module that displays a weather forcast.

%package -n mythtv-mythweb
Summary: 	The web interface to MythTV
Group: 		Video
Requires:	mythtv-backend >= %{version}
Requires:	php-mythtv >= %{version}
Requires:	apache-mod_php
Obsoletes:	mythweb < 0.20a-7

%description -n mythtv-mythweb
The web interface to MythTV.

%package -n mythtv-plugin-zoneminder
Summary:  Security camera plugin for MythTV
Group:    Video
Requires: mythtv-frontend >= %{version}

%description -n mythtv-plugin-zoneminder
A security camera plugin for MythTV.

%package -n mythtv-plugin-archive
Summary: 	Creates DVDs from your recorded shows
Group: 		Video
Requires:	dvd+rw-tools
Requires:	dvdauthor
Requires:	ffmpeg
Requires:	mjpegtools
Requires:	python-imaging
Requires:	python-mysql
Requires:	mythtv-frontend >= %{version}
%if %{build_plf}
Requires:	transcode
%endif
Requires:	cdrkit-genisoimage
Obsoletes:	mytharchive < 0.20a-7

%description -n mythtv-plugin-archive
MythArchive is a plugin for MythTV that lets you create DVDs
from your recorded shows, MythVideo files and any video files
available on your system. It can also archive recordings in a
proprietary format that archives not only the file but also all the
associated metadata like title, description and cut list information
which will mean you can create backups of myth recordings which can
later be restored or it will also allow you to move recordings
between myth systems without losing any of the metadata. It is a
complete rewrite of the old MythBurn bash scripts, now using python,
and the mythfrontend UI plugin.

%prep
%setup -q
%apply_patches

%build
%configure --enable-all --libdir-name=%{_lib} \
%if %{build_plf}
	--enable-mp3lame
%else
	--disable-mp3lame
%endif

%make

%install
%makeinstall INSTALL_ROOT=%{buildroot}

#mythgallery
mkdir -p %{buildroot}%{_localstatedir}/lib/pictures
#mythmusic
mkdir -p %{buildroot}%{_localstatedir}/lib/mythmusic

install -d -m755 %{buildroot}%{_var}/www/mythweb
install -m644 mythweb/*.php %{buildroot}%{_var}/www/mythweb
install -m755 mythweb/*.pl %{buildroot}%{_var}/www/mythweb

for dir in classes includes js modules skins ; do
  cp -r mythweb/$dir %{buildroot}%{_var}/www/mythweb
done

install -d -m755 %{buildroot}%{_localstatedir}/lib/mythweb/data
ln -s %{_localstatedir}/lib/mythweb/data %{buildroot}%{_var}/www/mythweb/data

# Create a default configuration for mythweb
install -d -m755 %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
install -m644 mythweb/mythweb.conf.apache %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf

perl -pi -e's|<Directory "/var/www/html|<Directory "%{_var}/www/mythweb|' %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf
perl -pi -e's|#    RewriteBase    /mythweb|    RewriteBase    /mythweb|' %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf

cat >> %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf <<EOF

# ROSA Customisations (be in sync with very sane Mageia's ones)

Alias /mythweb %{_var}/www/mythweb
<Directory %{_var}/www/mythweb>
    Order deny,allow
    Deny from all
    # Only allow localhost access by default. Customise to suit your needs
    # (customisations should be placed in a separate file in conf/vhosts.d/)
    Allow from 127.0.0.1
</Directory>
EOF

mkdir -p %{buildroot}%{_docdir}/mythtv-plugin-{browser,gallery,game,music,netvision,news,weather,video,zoneminder}

%files -n mythtv-plugin-browser
%doc mythbrowser/README mythbrowser/COPYING mythbrowser/AUTHORS
%{_libdir}/mythtv/plugins/libmythbrowser.so
%{_datadir}/mythtv/i18n/mythbrowser_*.qm
%{_datadir}/mythtv/themes/default*/browser-ui.xml
%{_datadir}/mythtv/themes/default*/mb_*.png

%files -n mythtv-plugin-gallery
%doc mythgallery/README*
%{_libdir}/mythtv/plugins/libmythgallery.so
%{_datadir}/mythtv/i18n/mythgallery_*.qm
%{_datadir}/mythtv/themes/default*/gallery*
%{_localstatedir}/lib/pictures

%files -n mythtv-plugin-game
%doc mythgame/romdb*
%{_libdir}/mythtv/plugins/libmythgame.so
%{_datadir}/mythtv/i18n/mythgame_*.qm
%{_datadir}/mythtv/game_settings.xml
%{_datadir}/mythtv/themes/default*/game*
%dir %{_datadir}/mythtv/metadata
%{_datadir}/mythtv/metadata/Game

%files -n mythtv-plugin-music
%doc mythmusic/AUTHORS mythmusic/COPYING mythmusic/README* mythmusic/musicdb
%{_datadir}/mythtv/music_settings.xml
%{_datadir}/mythtv/musicmenu.xml
%{_libdir}/mythtv/plugins/libmythmusic.so
%{_localstatedir}/lib/mythmusic
%{_datadir}/mythtv/i18n/mythmusic_*.qm
%{_datadir}/mythtv/themes/default/ff_button*.png
%{_datadir}/mythtv/themes/default*/mm_*.png
%{_datadir}/mythtv/themes/default*/mm-*.png
%{_datadir}/mythtv/themes/default/music-*.png
%{_datadir}/mythtv/themes/default*/*music*.xml
%{_datadir}/mythtv/themes/default/next_button*.png
%{_datadir}/mythtv/themes/default/pause_button*.png
%{_datadir}/mythtv/themes/default/play_button*.png
%{_datadir}/mythtv/themes/default/prev_button*.png
%{_datadir}/mythtv/themes/default/rew_button*.png
%{_datadir}/mythtv/themes/default/selectionbar.png
%{_datadir}/mythtv/themes/default/stop_button*.png
%{_datadir}/mythtv/themes/default/track_info_background.png
%{_datadir}/mythtv/themes/default/miniplayer_background.png
%{_datadir}/mythtv/themes/default-wide/music-sel-bg.png

%files -n mythtv-plugin-netvision
%doc mythnetvision/README mythnetvision/ChangeLog mythnetvision/AUTHORS
%{_bindir}/mythfillnetvision
%{_libdir}/mythtv/plugins/libmythnetvision.so
%{_datadir}/mythtv/i18n/mythnetvision_*.qm
%{_datadir}/mythtv/mythnetvision
%{_datadir}/mythtv/netvisionmenu.xml
%{_datadir}/mythtv/themes/default*/netvision*.xml

%files -n mythtv-plugin-news
%doc mythnews/AUTHORS mythnews/COPYING mythnews/ChangeLog mythnews/README*
%{_libdir}/mythtv/plugins/libmythnews.so
%{_datadir}/mythtv/i18n/mythnews_*.qm
%{_datadir}/mythtv/mythnews
%{_datadir}/mythtv/themes/default*/news*
%{_datadir}/mythtv/themes/default/enclosures.png
%{_datadir}/mythtv/themes/default/need-download.png
%{_datadir}/mythtv/themes/default/podcast.png

%files -n mythtv-plugin-weather
%doc mythweather/AUTHORS mythweather/COPYING mythweather/README*
%{_libdir}/mythtv/plugins/libmythweather.so
%{_datadir}/mythtv/i18n/mythweather_*.qm
%{_datadir}/mythtv/mythweather
%{_datadir}/mythtv/themes/default/cloudy.png
%{_datadir}/mythtv/themes/default/fair.png
%{_datadir}/mythtv/themes/default/flurries.png
%{_datadir}/mythtv/themes/default/fog.png
%{_datadir}/mythtv/themes/default/logo.png
%{_datadir}/mythtv/themes/default/lshowers.png
%{_datadir}/mythtv/themes/default/mcloudy.png
%{_datadir}/mythtv/themes/default/pcloudy.png
%{_datadir}/mythtv/themes/default/rainsnow.png
%{_datadir}/mythtv/themes/default/showers.png
%{_datadir}/mythtv/themes/default/snowshow.png
%{_datadir}/mythtv/themes/default/sunny.png
%{_datadir}/mythtv/themes/default/thunshowers.png
%{_datadir}/mythtv/themes/default/unknown.png
%{_datadir}/mythtv/themes/default*/mw*.png
%{_datadir}/mythtv/themes/default*/weather-ui.xml
%{_datadir}/mythtv/weather_settings.xml

%files -n mythtv-mythweb
%doc mythweb/README* mythweb/LICENSE mythweb/INSTALL mythweb/mythweb.conf.*
%{_var}/www/mythweb
%dir %{_localstatedir}/lib/mythweb
%attr(-,apache,apache) %{_localstatedir}/lib/mythweb/data
%config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/mythweb.conf

%files -n mythtv-plugin-zoneminder
%doc mythzoneminder/README mythzoneminder/COPYING mythzoneminder/AUTHORS
%{_bindir}/mythzmserver
%{_libdir}/mythtv/plugins/libmythzoneminder.so
%{_datadir}/mythtv/zonemindermenu.xml
%{_datadir}/mythtv/themes/default*/zoneminder*.xml
%{_datadir}/mythtv/themes/default*/mz_*.png
%{_datadir}/mythtv/i18n/mythzoneminder_*.qm

%files -n mythtv-plugin-archive
%{_bindir}/mytharchivehelper
%{_libdir}/mythtv/plugins/libmytharchive.so
%{_datadir}/mythtv/archive*.xml
%{_datadir}/mythtv/mytharchive
%{_datadir}/mythtv/themes/default/ma_*.png
%{_datadir}/mythtv/themes/default/mytharchive-ui.xml
%{_datadir}/mythtv/themes/default/mythburn-ui.xml
%{_datadir}/mythtv/themes/default/mythnative-ui.xml
%{_datadir}/mythtv/themes/default-wide/mytharchive-ui.xml
%{_datadir}/mythtv/themes/default-wide/mythburn-ui.xml
%{_datadir}/mythtv/themes/default-wide/mythnative-ui.xml
%{_datadir}/mythtv/i18n/mytharchive_*.qm


%changelog
* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0.24-20110303.2mdv2011.0
+ Revision: 645845
- relink against libmysqlclient.so.18
- rebuilt against mysql-5.5.8 libs, again

  + Colin Guthrie <cguthrie@mandriva.org>
    - s/mdkversion/mdvver/ macro conversion
    - Update to latest fixes

  + Anssi Hannula <anssi@mandriva.org>
    - plf: append "plf" to Release on cooker to make plf build have higher EVR
      again with the rpm5-style mkrel now in use

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.24-27174.3mdv2011.0
+ Revision: 626544
- rebuilt against mysql-5.5.8 libs

* Mon Nov 15 2010 Colin Guthrie <cguthrie@mandriva.org> 0.24-27174.1mdv2011.0
+ Revision: 597645
- Fix BuildRequires
- Fix build requires
- Add some extra build deps
- Reenable mythweather after packaging needed perl module.
- New version 0.24
 - Disable weather plugin just now as we don't have perl dep available yet.

* Thu Jun 17 2010 Colin Guthrie <cguthrie@mandriva.org> 0.23-25065.1mdv2010.1
+ Revision: 548212
- Update to latest fixes

* Tue May 25 2010 Colin Guthrie <cguthrie@mandriva.org> 0.23-24809.1mdv2010.1
+ Revision: 545864
- Updated to latest (post-release) -fixes

* Sun May 02 2010 Colin Guthrie <cguthrie@mandriva.org> 0.23-24305.1mdv2010.1
+ Revision: 541623
- New version: 0.23
- Update to latest -fixes

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-22864.2mdv2010.1
+ Revision: 509218
- rely on filetrigger for reloading apache configuration begining with 2010.1, rpm-helper macros otherwise

* Tue Nov 24 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22864.1mdv2010.1
+ Revision: 469801
- Update to latest fixes
- Enable libvisual visualisers

* Thu Nov 12 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22807.1mdv2010.1
+ Revision: 465510
- Update to post release -fixes.
- Latest upstream fixes-branch

* Tue Oct 13 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22416.0.1mdv2010.0
+ Revision: 457194
- Latest fixes

* Sun Oct 11 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22354.0.1mdv2010.0
+ Revision: 456639
- Latest updates
- Update to latest 0.22 code (currently trunk - release due shortly)
- Update lame patch for 0.22
- Re-enable mythbrowser (now based on Qt4's WebKit stuff)
- Drop old plugins controls and phone.
- General spec cleanup
- Mostly Harmless

* Tue Apr 14 2009 Colin Guthrie <cguthrie@mandriva.org> 0.21-20323.1mdv2009.1
+ Revision: 367224
- Update to latest fixes revision

* Sun Feb 22 2009 Colin Guthrie <cguthrie@mandriva.org> 0.21-19701.2mdv2009.1
+ Revision: 343884
- Package mythweb.pl in mythweb (mdv#46876)

* Sun Feb 15 2009 Colin Guthrie <cguthrie@mandriva.org> 0.21-19701.1mdv2009.1
+ Revision: 340530
- Fix filelist for mythflix
- Drop support for mythbrowser for now due to dependance on KDE3
- New fixes revision (r19701)

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against mysql-5.1.30 libs

* Sat Sep 27 2008 Colin Guthrie <cguthrie@mandriva.org> 0.21-18442.1mdv2009.0
+ Revision: 288919
- Update to -fixes revision r18442

  + Anssi Hannula <anssi@mandriva.org>
    - define %%_localstatedir locally for backportability

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Tue Mar 18 2008 Colin Guthrie <cguthrie@mandriva.org> 0.21-16507.2mdv2008.1
+ Revision: 188495
- Provide/Obsolete mythtv-plugin-dvd in mythtv-plugin-video

* Sat Mar 15 2008 Colin Guthrie <cguthrie@mandriva.org> 0.21-16507.1mdv2008.1
+ Revision: 188083
- Update to new fixes
- Fix mythweb packaging and config

* Sun Mar 02 2008 Colin Guthrie <cguthrie@mandriva.org> 0.21-0.16317.1mdv2008.1
+ Revision: 177563
- Add some more build requires
- Update fixes branch
- Prefix release by 0 to indicate pre-release.
- Remove copy/paste error
- Rediff the nolame patch for mythmusic
- Change how the mythweb configuration is generated
- Start tracking the 0.21-fixes branch in preparation for the official release

  + Thierry Vignaud <tv@mandriva.org>
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Colin Guthrie <cguthrie@mandriva.org> 0.20.2-14282.2mdv2008.0
+ Revision: 86033
- Rebuild

* Thu Aug 30 2007 Colin Guthrie <cguthrie@mandriva.org> 0.20.2-14282.1mdv2008.0
+ Revision: 76268
- Updateto 0.20.2 + fixes

* Tue Aug 14 2007 Colin Guthrie <cguthrie@mandriva.org> 0.20a-6.14191.1mdv2008.0
+ Revision: 63235
- Update to 'fixes' r14191

* Sun Apr 22 2007 Anssi Hannula <anssi@mandriva.org> 0.20a-6.13272.2mdv2008.0
+ Revision: 16867
- fix obsoletes

* Tue Apr 17 2007 Anssi Hannula <anssi@mandriva.org> 0.20a-6.13272.1mdv2008.0
+ Revision: 13901
- new snapshot
- Import mythplugins




* Fri Mar 23 2007 Anssi Hannula <anssi@mandriva.org> 0.20a-6.13114.1mdv2007.0
+ Revision: 148704
- drop patch1 (fixed upstream)
- new snapshot from the stable branch
- clean .spec
- add conditional plf build with lame and faad (patch2)
- rename packages to begin with mythtv-
- add requires python-imaging and python-mysql to mythtv-plugin-mytharchive
- bunzip2 patches
- Import mythplugins



* Sun Jan 21 2007 Stefan van der Eijk <stefan@zarb.org> 0.20a-6
- Remove patch backup files ".release-fixes"

* Sat Jan 20 2007 Stefan van der Eijk <stefan@zarb.org> 0.20a-5
- add release-0-20-fixes patch (12584)
- fix dependencies

* Sat Jan 13 2007 Stefan van der Eijk <stefan@zarb.org> 0.20a-4
- mythweb: fix includes symlink

* Fri Jan 12 2007 Stefan van der Eijk <stefan@zarb.org> 0.20a-3
- mythmusic: add patch0 for flac 1.1.3 support, from:
  ftp://ftp.altlinux.org/pub/people/thresh/
- mythweb: add includes symlink
- mythweb: add Requires: php-mysql

* Fri Sep 22 2006 Anssi Hannula <anssi@zarb.org> 0.20a-2plf2007.0
- fix requires

* Tue Sep 12 2006 Anssi Hannula <anssi@zarb.org> 0.20a-1plf2007.0
- 0.20a

* Sun Jul 16 2006 Anssi Hannula <anssi@zarb.org> 0.19.1-0.10553.1plf2007.0
- new snapshot of the stable branch
- fix buildrequires on cooker

* Sun Apr 23 2006 Anssi Hannula <anssi@zarb.org> 0.19-2plf
- fix PLF reason

* Tue Feb 21 2006 Anssi Hannula <anssi@zarb.org> 0.19-1plf
- 0.19
- clean spec
- rebuild buildrequires
- drop patch2, fixed upstream
- fix summary and description
- add mythflix
- drop mythphone post, user should know to read README anyway
- drop mythweb post, url is obvious
- make mythweb compliant to Mandriva Web Applications packaging Policy
- menus are not config files
- disable festival, it segfaults
- drop patch1, unneeded

* Thu Oct 13 2005 Anssi Hannula <anssi@zarb.org> 0.18.2-0.7468.1plf
- upgrade to release-0-18-fixes svn branch revision 7468
- remove patch1, fixed upstream
- remove mythcontrols, not present on this branch

* Mon Oct 10 2005 Anssi Hannula <anssi@zarb.org> 0.18.1-20050620.4plf
- fix changelog
- fix buildrequires libavc1394-devel
- fix x86_64 build (patch1)

* Mon Aug 22 2005 Stefan van der Eijk <stefan@zarb.org> 0.18.1-20050620.3plf
- no firewire support %%mdkversion > 1020
- add distsuffix
- %%mkrel
- start fixing changelog

* Wed Jul 06 2005 Stefan van derEijk <stefan@zarb.org> 0.18.1-20050620.2plf
- BuildRequires
- disable building with festival support
- remove -lmp4ff from makefile

* Mon Jun 20 2005 Austin Acton <austin@zarb.org> 0.18.1-20050620.1plf
- PLFify
- buildrequires libexif-devel
- disable festival on cooker
- clean up requires
- parallel build
- bump to cvs
- add mythcontrols

* Fri May 21 2005 Colin Guthrie <mythtv@colin.guthr.ie> 0.18.1-1.mdk10.2.thac
- Disable festival in x86_64 as this just segfaults mythphone. Will work on a more comprehensive fix.

* Fri May 20 2005 Colin Guthrie <mythtv@colin.guthr.ie> 0.18.1-1.mdk10.2.thac
- Build fixes for x86_64 (NB requires fixed festival/speechtools -fPIC libs)
- Bump version to 0.18.1 (from 0.18)

* Sun Feb 13 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.17-1.mdk10.1.thac
- Update to 0.17
- Sync with Axel Thimm spec file

* Mon Oct 25 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.16-4.mdk10.1.thac
- 4.mdk10.1.thac
- Where "4" is the release of the package, "mdk" is the distro, "10.1" is the release of the distro, and "thac" is the Torbjorn Turpeinen extension.

* Sat Oct 23 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.16-3thac
- Rebuilt for Mandrake 10.1

* Mon Sep 20 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.16-2thac
- Removed Prereq

* Sun Sep 12 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.16-1thac
- Updated to latest version
- Changed back to thac release to be able to support nnidia and via builds.

* Wed Jun 02 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.15.1-1plf
- Updated to latest version

* Fri May 28 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.15-1plf
- Updated to latest version

* Thu Apr 22 2004 Stefan van der Eijk <stefan@eijk.nu> 0.14-2plf
- BuildRequires

* Sun Feb 01 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.14-1plf
- Updated to latest version

* Wed Jan 14 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.13-4plf
- First plf release

* Fri Dec 18 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.13-3thac
- Cleaned up spec file

* Sun Dec 14 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.13-2thac
- Cleaned up spec file

* Sat Dec 13 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.13-1thac
- Compiled for Mandrake 9.2
