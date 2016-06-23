Name:		bass
Version:	2.4.12
Release:	1%{?dist}
Summary:	BASS is an audio library for use in software on several platforms

Group:		Development/Libraries
License:	Free for non-commercial use.
URL:		http://www.un4seen.com/bass.html
Source0:	bass24-linux.zip
NoSource:	0

%description
BASS is an audio library for use in software on several platforms. Its
purpose is to provide the powerful and efficient sample, stream, MOD
music, and recording functions. All in a compact DLL that won't overly
bloat your software.

%prep
cd "$RPM_BUILD_DIR"
rm -rf bass24-linux
unzip -qq -d $RPM_BUILD_DIR/bass24-linux $RPM_SOURCE_DIR/bass24-linux.zip

%install

mkdir -p "$RPM_BUILD_ROOT%{_includedir}/"
mkdir -p "$RPM_BUILD_ROOT%{_libdir}/"

cp $RPM_BUILD_DIR/bass24-linux/bass.h "$RPM_BUILD_ROOT%{_includedir}/"

echo "libdir: %{_includedir}"
case $RPM_ARCH in
"x86_64")
	cp $RPM_BUILD_DIR/bass24-linux/x64/libbass.so "$RPM_BUILD_ROOT%{_libdir}/"
	;;
*)
	cp $RPM_BUILD_DIR/bass24-linux/libbass.so "$RPM_BUILD_ROOT%{_libdir}/"
	;;
esac


%files
%{_includedir}/bass.h
%{_libdir}/libbass.so

%changelog

