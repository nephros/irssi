Name:           irssi
Version:        1.2.3
Release:        1
Summary:        Modular, Secure, and Well Designed IRC Client
License:        GPLv2
Group:          Productivity/Networking/IRC
URL:            http://www.irssi.org
Distribution:	SailfishOS
Packager:	szopin
Source:         irssi-%{version}.tar.xz
# deps for autogen.sh
BuildRequires: make
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  openssl-devel
BuildRequires:	gcc
BuildRequires:	glib2-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig


%description
Irssi is a modular IRC client for UNIX that currently only has a text
mode user interface. However, 80-90% of the code is not text mode
specific, so other UIs could be created easily. Also, Irssi is not
really even IRC specific anymore. There are already working SILC and
ICB modules available. Support for other protocols, like ICQ and
Jabber, could be added some day, too.

It is the code that separates Irssi from ircII, BitchX, epic, and the
rest of the text clients. It is not using the ircII code.

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
sed -i 's/git log/#git log/g' autogen.sh
./autogen.sh
%configure %{nil}
%make_build

%install
%make_install

%files
%config(noreplace) %{_sysconfdir}/irssi.conf
%{_bindir}/irssi
%doc /usr/share/doc/irssi/*
# scripts & themes
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/irssi/*
%exclude /usr/lib/pkgconfig/irssi-1.pc
%exclude /usr/lib64/pkgconfig/irssi-1.pc
/usr/share/man/man1/irssi.1.gz

%if 0%{?sailfishos_version} >= 50100
%files perl
%perl_archlib/*/Irssi.pm
%perl_archlib/*/Irssi/*.pm
%perl_archlib/*/auto/Irssi/*
%perl_archlib/*/auto/Irssi/.packlist
%perl_archlib/*/perllocal.pod
%endif
%changelog
