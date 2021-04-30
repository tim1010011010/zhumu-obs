Name:		zhumu
Version:	2.5.361956.0302
Release:    0
Summary: 	Zhumu installer
License:    SUSE-NonFree
Group:      Productivity/Networking/Other
Url:		https://www.zhumu.com/
Source:		zhumu-2.5.361956.0302.tar.bz2
ExclusiveArch:  x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Video Conferencing and Web Conferencing Service

%prep
%setup -q

%build

%install
install -d %{buildroot}/opt
install -d %{buildroot}%{_datadir}/applications/
install -d %{buildroot}%{_datadir}/doc/
install -d %{buildroot}%{_datadir}/doc/zhumu/
install -d %{buildroot}%{_datadir}/mime/
install -d %{buildroot}%{_datadir}/mime/packages/
install -d %{buildroot}%{_datadir}/pixmaps/
install -d %{buildroot}%{_bindir}
cp -rf opt/zhumu  %{buildroot}/opt/zhumu
cp -rf usr/share/doc/zhumu %{buildroot}%{_datadir}/doc/zhumu
cp -r usr/share/mime/packages/zhumu.xml %{buildroot}%{_datadir}/mime/packages/zhumu.xml
cp -f usr/share/pixmaps/application-x-zhumu.png %{buildroot}%{_datadir}/pixmaps/application-x-zhumu.png
cp -f usr/share/pixmaps/Zhumu.png %{buildroot}%{_datadir}/pixmaps/Zhumu.png
ln -s /opt/zhumu/zhumu %{buildroot}%{_bindir}/zhumu
echo "[Desktop Entry]
Categories=Application;Network;Chat;
Name=Zhumu
GenericName=Zhumu Video Conference
Comment=Zhumu Video Conference
Exec=/usr/bin/zhumu %U
Terminal=false
Type=Application
Icon=/usr/share/pixmaps/Zhumu.png
StartupWMClass=zhumu
X-Desktop-File-Install-Version=%{version}" > %{buildroot}%{_datadir}/applications/zhumu.desktop


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/opt/zhumu
%{_bindir}/zhumu
%{_datadir}/applications/zhumu.desktop
%{_datadir}/doc
%{_datadir}/doc/zhumu
%{_datadir}/mime
%{_datadir}/mime/packages
%{_datadir}/mime/packages/zhumu.xml
%{_datadir}/pixmaps
%{_datadir}/pixmaps/application-x-zhumu.png
%{_datadir}/pixmaps/Zhumu.png

%changelog
