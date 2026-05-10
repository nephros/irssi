Name:           irssi
Version:        1.4.5
Release:        1
Summary:        Modular, Secure, and Well Designed IRC Client
License:        GPLv2
Group:          Productivity/Networking/IRC
URL:            http://www.irssi.org
Distribution:	SailfishOS
Packager:	szopin
Source:         irssi-%{version}.tar.xz
BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(ncursesw)


%description
Irssi is a modular IRC client for UNIX that currently only has a text
mode user interface. However, 80-90% of the code is not text mode
specific, so other UIs could be created easily. Also, Irssi is not
really even IRC specific anymore. There are already working SILC and
ICB modules available. Support for other protocols, like ICQ and
Jabber, could be added some day, too.

It is the code that separates Irssi from ircII, BitchX, epic, and the
rest of the text clients. It is not using the ircII code.

%if 0%{?_chum}
Type: console-application
PackagedBy: szopin
Custom:
  Repo: https://codeberg.org/irssi/irssi
  PackagingRepo: https://github.com/szopin/irssi
PackageIcon: https://codeberg.org/repo-avatars/50076-0df574274780a2044751384f596a2cb9
Links:
  Homepage: %{url}
%endif


%package devel
Summary:    Development headers and libraries for irssi.
Requires:   %{name} = %{version}-%{release}

%description devel
Irssi development headers

%if 0%{?sailfishos_version} >= 50100
%package perl
Summary:    Perl package for irssi.

%description perl
Irssi perl library
%endif

%prep

%setup -q -n %{name}-%{version}/irssi

%build
%meson
%meson_build

%install
%meson_install

%files
#%%config(noreplace) %%{_sysconfdir}/irssi.conf
%{_bindir}/irssi
%doc /usr/share/doc/irssi/*
# scripts & themes
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/irssi/*
%exclude %{_libdir}/pkgconfig/irssi-1.pc
%{_mandir}/man1/irssi.1.gz

%if 0%{?sailfishos_version} >= 50100
%files perl
%dir %{_libdir}/irssi
%{_libdir}/irssi/modules/*.so
%perl_archlib/*/Irssi.pm
%perl_archlib/*/Irssi/*.pm
%perl_archlib/*/auto/Irssi/*
#%%perl_archlib/*/auto/Irssi/.packlist
#%%perl_archlib/*/perllocal.pod
%endif
%changelog
