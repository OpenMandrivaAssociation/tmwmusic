Name:		tmwmusic
Version:	0.2
Release:	%mkrel 2
Summary:	The music for The Mana World
Group:		Games/Other
License:	GPLv2+
Url:		http://themanaworld.org/
Source0:	http://downloads.sourceforge.net/themanaworld/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Suggests:	tmw

%description
This packages contains the music for The Mana World.

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesdatadir}/tmw/
cp -R data %{buildroot}%{_gamesdatadir}/tmw/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{_gamesdatadir}/tmw
