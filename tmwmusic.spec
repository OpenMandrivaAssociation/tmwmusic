Name:		tmwmusic
Version:	0.3
Release:	1
Summary:	The music for The Mana World
Group:		Games/Other
License:	GPLv2+
Url:		http://themanaworld.org/
Source0:	http://sourceforge.net/projects/themanaworld/files/TMW%20Music/0.3/%{name}-%{version}.tar.gz
BuildArch:	noarch

Suggests:	tmw

%description
This packages contains the music for The Mana World.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_gamesdatadir}/tmw/
cp -R data %{buildroot}%{_gamesdatadir}/tmw/

%clean

%files
%defattr(0644,root,root,0755)
%{_gamesdatadir}/tmw


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdv2011.0
+ Revision: 615231
- the mass rebuild of 2010.1 packages

* Tue Jan 05 2010 Jérôme Brenier <incubusss@mandriva.org> 0.2-1mdv2010.1
+ Revision: 486409
- import tmwmusic



