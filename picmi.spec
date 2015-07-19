Name:		picmi
Version:	15.04.3
Release:	2
Summary:	A nonogram logic game for KDE
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://games.kde.org/game.php?game=picmi
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	kdelibs4-devel
BuildRequires: 	cmake(KDEGames)


%description
Picmi is a number logic game in which cells in a grid have to be colored or
left blank according to numbers given at the side of the grid to reveal a
hidden picture.

%files
%{_bindir}/picmi                                                                                       
%{_datadir}/applications/kde4/picmi.desktop                                                            
%{_datadir}/apps/picmi/                                                                                
%{_iconsdir}/hicolor/*/apps/picmi.*                                                                    
%doc %{_docdir}/HTML/en/picmi
#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

