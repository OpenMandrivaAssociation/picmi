%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		picmi
Version:	17.11.90
Release:	1
Summary:	A nonogram logic game for KDE
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://games.kde.org/game.php?game=picmi
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires: 	cmake(KF5KDEGames)
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Test)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:  cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Init)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5CoreAddons)

%description
Picmi is a number logic game in which cells in a grid have to be colored or
left blank according to numbers given at the side of the grid to reveal a
hidden picture.

%files -f %{name}.lang
%{_bindir}/picmi
%{_datadir}/applications/org.kde.picmi.desktop
%{_datadir}/kxmlgui5/picmi
%{_datadir}/picmi
%{_datadir}/metainfo/org.kde.picmi.appdata.xml
%{_iconsdir}/hicolor/*/apps/picmi.*
#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
