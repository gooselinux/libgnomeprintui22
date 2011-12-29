%define gtk2_version 2.4.0
%define libgnomeprint_version 2.10.0
%define libgnomecanvas_version 2.3.0
%define gettext_package libgnomeprintui-2.2

Summary: GUI support for libgnomeprint
Name: libgnomeprintui22
Version: 2.18.4
Release: 3%{?dist}
Source0: http://ftp.gnome.org/pub/gnome/sources/libgnomeprintui/2.18/libgnomeprintui-%{version}.tar.bz2
URL: http://ftp.gnome.org/pub/gnome/sources/libgnomeprintui/
License: LGPLv2+
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gtk2-devel >= %{gtk2_version}
BuildRequires:  libgnomeprint22-devel >= %{libgnomeprint_version}
BuildRequires:  libgnomecanvas-devel >= %{libgnomecanvas_version}
BuildRequires:  fontconfig-devel
BuildRequires:  gnome-icon-theme >= 1.2.0
BuildRequires:  gettext
BuildRequires:  intltool

# updated translations
# https://bugzilla.redhat.com/show_bug.cgi?id=589221
Patch0: libgnomeprintui22-translations.patch

%description

The libgnomeprintui package contains GTK+ widgets related to printing.

%package devel
Summary: Libraries and headers for libgnomeprintui
Group: Development/Libraries
Requires: %name = %{version}-%{release}

Requires:  pkgconfig
Requires:  gtk2-devel >= %{gtk2_version}
Requires:  libgnomeprint22-devel >= %{libgnomeprint_version}
Requires:  libgnomecanvas-devel >= %{libgnomecanvas_version}

%description devel

The libgnomeprintui package contains GTK+ widgets related to printing.

You should install the libgnomeprintui-devel package if you would like
to compile applications that use the widgets in libgnomeprintui. You
do not need to install it if you just want to use precompiled
applications.

%prep
%setup -q -n libgnomeprintui-%{version}
%patch0 -p1 -b .translations

%build
%configure --disable-gtk-doc --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%find_lang %{gettext_package}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{gettext_package}.lang
%defattr(-,root,root)

%doc AUTHORS COPYING NEWS README

%{_libdir}/lib*.so.*
%{_datadir}/libgnomeprintui

%files devel
%defattr(-,root,root)

%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/libgnomeprintui

%changelog
* Wed Jun 23 2010 Matthias Clasen <mclasen@redhat.com> - 2.18.4-3
- Updated translations
Resolves: #589221

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.18.4-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.4-1
- Update to 2.18.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.18.3-1
- Update to 2.18.3

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.18.2-2
- fix license tag

* Thu Jan 31 2008 Matthias Clasen <mclasen@redhat.com> - 2.18.2-1
- Update to 2.18.2

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.1-1
- Update to 2.18.1

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 2.18.0-2
- Rebuild for build ID

* Tue Mar 13 2007 Matthias Clasen  <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Tue Feb 27 2007 Matthias Clasen  <mclasen@redhat.com> - 2.17.92-1
- Update to 2.17.92

* Tue Feb 13 2007 Matthias Clasen  <mclasen@redhat.com> - 2.17.91-1
- Update to 2.17.91

* Tue Jan 23 2007 Matthias Clasen  <mclasen@redhat.com> - 2.17.90-1
- Update to 2.17.90

* Sun Nov 12 2006 Matthias Clasen  <mclasen@redhat.com> - 2.17.0-1
- Update to 2.17.0
- Don't ship static libraries
- Require pkgconfig in the -devel package

* Thu Aug 24 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-6
- Add patch to fix print preview crashes (RH bug #201155).

* Fri Jul 28 2006 Matthias Clasen  <mclasen@redhat.com> - 2.12.1-5
- Re-add docs

* Thu Jul 27 2006 Matthias Clasen  <mclasen@redhat.com> - 2.12.1-4
- Disable gtk-doc to fix multilib conflicts

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.12.1-3.1
- rebuild

* Mon Jun 12 2006 Bill Nottingham <notting@redhat.com> - 2.12.1-3
- buildreq automake, not automake16
- buildreq gettext

* Mon Jun  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.12.1-2
- Rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.12.1-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.12.1-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Sep 30 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.1-1
- Update to 2.12.1

* Mon Sep  7 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.0-1
- Update to 2.12.0

* Tue Aug 16 2005 Matthias Clasen <mclasen@redhat.com> 
- Rebuilt

* Mon Jul 11 2005 Matthias Clasen <mclasen@redhat.com> - 2.11.0-1
- Newer upstream version

* Fri Mar 18 2005 David Zeuthen <davidz@redhat.com> - 2.10.1-1
- New upstream version - drop a patch that was merged upstream

* Fri Mar  4 2005 David Zeuthen <davidz@redhat.com> - 2.8.2.-2
- Rebuild

* Thu Jan 27 2005 Matthias Clasen <mclasen@redhat.com> - 2.8.2-1
- Update to 2.8.2

* Tue Oct 26 2004 Colin Walters <otaylor@redhat.com> - 2.8.0-2
- Add patch libgnomeprintui-2.8.0-selector-search.patch for
  interactively searching for a printer

* Mon Sep 27 2004 Owen Taylor <otaylor@redhat.com> - 2.8.0-1
- Version 2.8.0

* Tue Aug 31 2004 Matthias Clasen <mclasen@redhat.com> 2.7.1-7
- Fix handling of selection changes when the previously
  selected printer is gone.  (#131626)

* Tue Aug 31 2004 Matthias Clasen <mclasen@redhat.com> 2.7.1-5
- Fix the initial selection of the default printer.

* Tue Aug  3 2004 Owen Taylor <otaylor@redhat.com> 2.7.1-3
- Update to real 2.7.1 tarball
- Remove --enable-gtk-doc again
- Add build requires for gtk-doc and gnome-icon-theme (#124935,
  Maxim Dzumanenko)

* Thu Jul 29 2004 Colin Walters <walters@redhat.com> 2.7.1-2
- Add patch which fixes default printer case, minor threading bugs

* Thu Jul 08 2004 Colin Walters <walters@redhat.com> 2.7.1-1
- Update to latest upstream CVS (20040708)
- Merge dynamism patch with upstream CVS

* Thu Jun 17 2004 Matthias Clasen <mclasen@redhat.com> 2.7.0-2
- Show printers in a tree view.

* Tue Jun 15 2004 Colin Walters <walters@redhat.com> 2.7.0-1
- Update to 2.7.0 CVS
- Pass --enable-gtk-doc to configure
- Add current version of patch which handles dynamic updating
  from libgnomeprint.
- Bump required libgnomeprint version.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr  1 2004 Alex Larsson <alexl@redhat.com> 2.6.0-1
- update to 2.6.0

* Fri Mar 12 2004 Alex Larsson <alexl@redhat.com> 2.5.4-1
- update to 2.5.4

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 26 2004 Alexander Larsson <alexl@redhat.com> 2.5.3-1
- update to 2.5.3

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 28 2004 Alexander Larsson <alexl@redhat.com> 2.5.1-1
- update to 2.5.1

* Wed Jan  7 2004 Owen Taylor <otaylor@redhat.com> 2.4.2-1
- Update 2.4.2 to get some crasher fixes

* Tue Oct 28 2003 Owen Taylor <otaylor@redhat.com> 2.4.0-1
- Update to 2.4.0

* Thu Sep 11 2003 Jeremy Katz <katzj@redhat.com> 2.3.1-2
- remove spurious comma in gnome-print-dialog.h that causes errors with 
  gcc 3.3 and -pedantic

* Tue Aug 19 2003 Alexander Larsson <alexl@redhat.com> 2.3.1-1
- update for gnome 2.3

* Wed Jul  9 2003 Owen Taylor <otaylor@redhat.com> 2.2.1.3-2.0
- Bump for rebuild

* Wed Jul  2 2003 Owen Taylor <otaylor@redhat.com> 2.2.1.3-1
- Version 2.2.1.3

* Thu Jun 12 2003 Owen Taylor <otaylor@redhat.com> 2.2.1.2-1
- Version 2.2.1.2

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb  4 2003 Alexander Larsson <alexl@redhat.com>
- 2.2.1.1

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan 16 2003 Havoc Pennington <hp@redhat.com>
- 2.1.8

* Mon Dec 16 2002 Havoc Pennington <hp@redhat.com>
- initial build of libgnomeprintui 2.2 (version 2.1.4)

