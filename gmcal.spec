Summary:	GTK+ libmcal powered calendar
Summary(pl):	Oparty o libmcal kalendarz z interfejsem GTK+
Name:		gmcal
Version:	0.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/libmcal/%{name}-%{version}.tar.gz
URL:		http://mcal.chek.com/
BuildRequires:	gtk+-devel
BuildRequires:	libmcal-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is a very early release of a GTK+ app that can display you
calendar and appointment either via mstore or ICAP protocol drivers.

%description -l pl
To jest wczesna wersja aplikacji GTK+ potrafi�cej wy�wietlaj��
kalendarz i terminy spotka� korzystaj�c z protoko�u mstore lub ICAP.

%prep
%setup -q -n %{name}

%build
%{__cc} -I/usr/include/mcal %{rpmcflags} %{rpmldflags} \
	gmcal.c -o gmcal -lmcal -lcrypt `gtk-config --cflags --libs`

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install gmcal $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
