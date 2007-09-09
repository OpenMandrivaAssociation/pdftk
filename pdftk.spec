%define name pdftk
%define version 1.41
%define release %mkrel 3

%define gcj_version %(gcj --version | head -n 1 | awk '{print $3}')

Summary: 	Pdftk stand for Pdf Tool Kit
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{name}-%{version}.tar.bz2
License: 	GPL
Group: 		Publishing
Url: 		http://www.accesspdf.com/pdftk/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	libgcj-devel
BuildRequires: 	gcc-java > 3

%description
Pdftk is a simple tool for doing everyday things with PDF documents.
Keep one in the top drawer of your desktop and use it to:
- Merge PDF Documents
- Split PDF Pages into a New Document
- Decrypt Input as Necessary (Password Required)
- Encrypt Output as Desired
- Fill PDF Forms with FDF Data and/or Flatten Forms
- Apply a Background Watermark
- Report on PDF Metrics, including Metadata and Bookmarks
- Update PDF Metadata
- Attach Files to PDF Pages or the PDF Document
- Unpack PDF Attachments
- Burst a PDF Document into Single Pages
- Uncompress and Re-Compress Page Streams
- Repair Corrupted PDF (Where Possible)

%prep
%setup -q

%build
cd pdftk
%__perl -pi -e 's|VERSUFF=.*|VERSUFF= -%{gcj_version}|' Makefile.Mandrake
%__perl -pi -e 's|CXXFLAGS=|CXXFLAGS+=|' Makefile.Mandrake

export CXXFLAGS=$RPM_OPT_FLAGS

# Work around for a buggy gcj configuration on the cluster:
export CLASSPATH=./
make -f Makefile.Mandrake 

%install
rm -rf $RPM_BUILD_ROOT
%__install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
%__install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
%__perl -pi -e "s/\r\n/\n/" pdftk.1.txt
%__install -m755 pdftk/pdftk -D $RPM_BUILD_ROOT%{_bindir}/pdftk

%__bzip2 debian/pdftk.1
%__install -m755 debian/pdftk.1.bz2 -D $RPM_BUILD_ROOT%{_mandir}/man1/pdftk.1.bz2

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc pdftk.1.html pdftk.1.txt
%{_mandir}/man1/pdftk.1*
%{_bindir}/pdftk


