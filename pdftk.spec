%define gcj_support 1

Name:		pdftk
Version:	2.02
Release:	3
Summary:	PDF Tool Kit
License:	GPLv2+
Group:		Publishing
URL:		http://www.pdfhacks.com/pdftk/
Source0:	http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/%{name}-%{version}-src.zip
Patch0:		bug-427046_pdftk.cc.patch
BuildRequires:  gcc-java
BuildRequires:  gcc-c++
BuildRequires:	java-devel
BuildRequires:	pkgconfig(libgcj-4.9)
BuildRequires:	unzip
BuildRequires:	fastjar
BuildRequires:	dos2unix
Requires:	bouncycastle

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
%setup -q -n %{name}-%{version}-dist
%patch0 -p0
%__sed -i 's/\r$//' changelog.txt license_gpl_pdftk/*.txt license_gpl_pdftk/*/*.txt
%__chmod 644 changelog.txt license_gpl_pdftk/*.txt license_gpl_pdftk/*/*.txt

%build
pushd pdftk
	GCJFLAGS="%{optflags} -I`pwd`/../java -Wno-all" make -f Makefile.Redhat
popd

 
%install
%__install -Dm 0755 pdftk/%name %{buildroot}%{_bindir}/%name
%__install -Dpm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%clean
%__rm -rf %buildroot

%files
%{_bindir}/%name
%{_mandir}/man1/%{name}.*
%doc changelog.txt license_gpl_pdftk/*.txt license_gpl_pdftk/*/*.txt
