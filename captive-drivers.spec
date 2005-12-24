# the drivers that were supposed to work, didn't.
# so these drivers didn't work for me.
Summary:	NTFS Drivers
Summary(pl):	Sterowniki NTFS
Name:		captive-drivers
Version:	0.1
Release:	0.2
License:	restricted, non-distributable
Group:		Applications/System
Source0:	http://download.microsoft.com/download/9/7/6/9763833d-bd58-41e2-9911-50f64c7252a3/xpsp1a_en_x86_CHK.exe
# NoSource0-md5:	257c90b85f20f597caad8a4bd8c481ef
NoSource:	0
BuildRequires:	cabextract
Requires:	captive
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Contains ntfs.sys and ntoskrnl.exe from Windows XP SP1.

%description -l pl
Pakiet zawieraj±cy ntfs.sys i ntoskrnl.exe z Windows XP SP1.

%prep
%setup -q -c -T
cabextract %{SOURCE0} -F ntfs.sys
cabextract %{SOURCE0} -F ntoskrnl.ex_
cabextract ntoskrnl.ex_

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/captive
install ntfs.sys ntoskrnl.exe $RPM_BUILD_ROOT/var/lib/captive

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/var/lib/captive/*
